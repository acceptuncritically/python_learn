from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from file_history_store import get_history
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from langchain_deepseek import ChatDeepSeek
import config_data as config
from vector_stores import VectorStores
from operator import itemgetter


class RagService(object):
    def __init__(self):
        self.vector_stores = VectorStores(
            # ✅ 入库(knowledge_base.py)和检索(这里)必须使用同一套向量模型配置，
            #    统一由 config.get_embeddings() 创建，保证两边向量在同一个空间。
            embedding=config.get_embeddings()
        )
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "按照我提供的资料为主，和历史信息如下，简洁地回答问题，参考资料:{context}。"),
                MessagesPlaceholder("history"),
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

        # ❌ 原代码：
        #     chain = (
        #         {
        #             "input": RunnablePassthrough(),
        #             "context": retriever | format_document,
        #         }
        #         | self.prompt_template | self.chat_model | StrOutputParser()
        #     )
        #    这种写法的隐患是：字典里的每个子链拿到的都是【整个输入字典】而不是
        #    用户的问题本身，于是：
        #      1) retriever 收到的查询是 {"input": "...", "history": [...]} 这样的 dict，
        #         Chroma 把它原样交给智谱向量接口 → 智谱返回
        #         400 {"error":{"code":"1210","message":"API 调用参数有误，请检查文档。"}}。
        #         这就是“一调用智谱向量模型就报错”的真正原因：
        #         请求参数格式不对，而不是 API Key / 网络问题。
        #      2) prompt 里的 {input} 也会被填成整个字典；
        #      3) 输入字典里的 history 键会被丢掉，MessagesPlaceholder("history") 缺变量。
        # ✅ 修正：用 itemgetter("input") 只把“用户问题”取出来喂给 retriever；
        #          用 RunnablePassthrough.assign 保留原输入字典（含 history）并追加 context。
        chain = (
            RunnablePassthrough.assign(
                context=itemgetter("input") | retriever | format_document,
            )
            | self.prompt_template
            | self.chat_model
            | StrOutputParser()
        )
        conversation_chain=RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="input",
            history_messages_key="history",
        )
        return conversation_chain


if __name__ == "__main__":
    rag_service = RagService()
    run_config = {
        "configurable": {"session_id": "test_session_id"}
    }
    print(rag_service.chain.invoke(input={"input": "你好，公司上午几点上班"}, config=run_config))
