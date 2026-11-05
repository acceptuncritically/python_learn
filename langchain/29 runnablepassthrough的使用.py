"""
为了保证将28的向量检索问题，也能够入链，我们使用RunnablePassthrough类来实现
由于InMemoryVectorStore不支持Runnable接口，无法加入链
langchain中向量存储对象 有一个方法as_retriever()可以返回一个runnable接口的子类对象
"""
from langchain_core.documents import Document
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_deepseek import ChatDeepSeek
import os
model = ChatDeepSeek(model="deepseek-chat", temperature=0.7)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料:{context}。"),
        ("user", "用户提问: {input}")
    ]
)
ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")

embeddings = OpenAIEmbeddings(
    model="embedding-3",  # 智谱的嵌入模型
    openai_api_key=ZHIPU_API_KEY,
    openai_api_base="https://open.bigmodel.cn/api/paas/v4",
)
vector_store = InMemoryVectorStore(embeddings)

# 准备一下资料（向量库的数据）
# add_texts 传入一个 list[str]
vector_store.add_texts(["减肥就是要少吃多练", "在减脂期间吃东西很重要,清淡少油控制卡路里摄入并运动起来", "跑步是很好的运动"])

input_text = "怎么减肥?"

retriever=vector_store.as_retriever(search_kwargs={"k":2})

def format_fun(docs:list[Document]):
    if not docs:
        return "无相关参考资料"
    formatted_str=""
    for doc in docs:
        formatted_str+=doc.page_content
    formatted_str+="]"
    return formatted_str

#将其加入链
chain = {"input":RunnablePassthrough(),"context":retriever|format_fun}|prompt | model | StrOutputParser()
#通过invoke将内容一分为二 传给input 和context 由于retriever的输入要求是字符串 invoke里写字符串
res=chain.invoke(input_text)
print(res)

"""
retriever:
    输入：用户的提问            str
    输出：向量库检索相关的参考资料 list[document]  
prompt：
    输入：向量库检索用户提问和相关的参考资料 dict
    输出：用户问题的答案                  promptvalue 
"""
