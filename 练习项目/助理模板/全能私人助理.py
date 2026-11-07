from langchain_core.runnables import RunnableLambda
import os
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
str_parser=StrOutputParser()
my_function=RunnableLambda(lambda x:print("小助理正在思考..."))
model=ChatDeepSeek(model="deepseek-chat",temperature=0.7)
prompt = ChatPromptTemplate.from_template("你是一个私人助理你要根据我的问题做出不同的回答"
        "如果我的问题是日常闲聊类的你就直接以字符串的方式返回问题的答案，如果我的问题是具体业务逻辑你就直接返回work字符串"
"这是我的问题：{question}")
embeddings = OpenAIEmbeddings(
    model="embedding-3",  # 智谱的嵌入模型
    openai_api_key=os.environ["ZHIPU_API_KEY"],
    openai_api_base="https://open.bigmodel.cn/api/paas/v4",
)
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
loader = TextLoader(
    file_path="faq.txt",
    encoding="utf-8",
)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
    separators=["\n\n", "\n", "。", "！", "？", " ", ""]
)
vector_store = InMemoryVectorStore(embeddings)
vector_store.add_documents(text_splitter.split_documents(loader.load()))
"""
as_retriever() 方法的作用就是做一个轻量级的“包装”。它接收 vector_store 对象，
并返回一个 VectorStoreRetriever 实例。这个实例内部仍然使用 vector_store 进行实际的搜索，
但对外暴露的却是标准的检索器接口（如 invoke 或 get_relevant_documents）。
"""
retriever = vector_store.as_retriever(search_kwargs={"k": 10})

intent_chain = prompt | model | str_parser
#构建两个不同的链一个是聊天链
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是我的女朋友想办法为我排忧解难，要求语气温和。"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])
chat_chain = chat_prompt | model | str_parser
#构建一个RAG链
rag_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个公司业务助理。请严格基于以下检索到的上下文回答问题：\n{context}"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])
from operator import itemgetter
def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])
rag_chain = (
        {
            # 分支1：提取字典中的 question，去检索，拼接成 context 字符串
            "context": itemgetter("question") | retriever | format_docs,
            # 分支2：原样传递字典中的 question
            "question": itemgetter("question"),
            # 分支3：原样传递字典中的 history
            "history": itemgetter("history")
        }
        | rag_prompt  # 此时 rag_prompt 会收到一个完美的包含三个键的字典
        | model
        | str_parser
)
if __name__ == "__main__":
    chat_history=[]
    while True:
        print("我们开始做点什么？(exit退出)")
        question = input("用户: ")
        if question == "exit":
            break
        intent = intent_chain.invoke({"question": question, "history": chat_history})
        if "work" in intent:
            response=rag_chain.stream({"question": question, "history": chat_history})
            for chunk in response:
                print(chunk, end="", flush=True)
            print()
        else:
            response=chat_chain.stream({"question": question, "history": chat_history})
            for chunk in response:
                print(chunk, end="", flush=True)
            print()

