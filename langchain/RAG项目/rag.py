from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os

from langchain_core.runnables import RunnablePassthrough
from langchain_deepseek import ChatDeepSeek
import config_data as config
from vector_stores import VectorStores
# ✅ 修正：使用官方独立包，避免 langchain_community 的弃用警告
from langchain_openai import OpenAIEmbeddings

ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")


class RagService(object):
    def __init__(self):
        self.vector_stores = VectorStores(
            embedding=OpenAIEmbeddings(
                model="embedding-3",  # 智谱的嵌入模型
                openai_api_key=ZHIPU_API_KEY,
                openai_api_base="https://open.bigmodel.cn/api/paas/v4",
            )
        )
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "按照我提供的资料为主，简洁地回答问题，参考资料:{context}。"),
                ("user", "{input}"),
            ]
        )
        # 说明：ChatDeepSeek 默认读取环境变量 DEEPSEEK_API_KEY，
        # 你的系统用户变量里已经配置好了，所以这里不用再传 api_key。
        self.chat_model = ChatDeepSeek(model=config.chat_model, temperature=0.7)
        self.chain = self.__get_chain()

    def __get_chain(self):
        # 获取最终的链
        retriever = self.vector_stores.get_retriever()

        def format_document(docs):
            if not docs:
                return "无相关参考资料"
            # ✅ 修正：多个分块之间用换行分隔，避免文字直接粘在一起
            return "\n\n".join(doc.page_content for doc in docs)

        chain = (
            {
                "input": RunnablePassthrough(),
                "context": retriever | format_document,
            } | self.prompt_template | self.chat_model | StrOutputParser()
        )
        return chain


if __name__ == "__main__":
    rag_service = RagService()
    print(rag_service.chain.invoke("你好，公司上午几点上班"))
