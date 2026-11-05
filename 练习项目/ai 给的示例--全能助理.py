import os
from langchain_core.runnables import RunnableLambda, RunnableBranch, RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_deepseek import ChatDeepSeek

# ================= 1. 环境准备与基础设置 =================
# 假设你已经设置了 ZHIPU_API_KEY 和 DEEPSEEK_API_KEY 环境变量
model = ChatDeepSeek(model="deepseek-chat", temperature=0.7)
str_parser = StrOutputParser()

# 准备测试用的 faq.txt (如果本地没有的话)
if not os.path.exists("faq.txt"):
    with open("faq.txt", "w", encoding="utf-8") as f:
        f.write("公司年假规定：员工入职满一年后，每年享有 5 天带薪年假。满三年享有 10 天。\n"
                "公司打卡规定：每天上午 9:30 前需完成打卡。")

embeddings = OpenAIEmbeddings(
    model="embedding-3",
    openai_api_key=os.environ["ZHIPU_API_KEY"],
    tiktoken_enabled=False,
    openai_api_base="https://open.bigmodel.cn/api/paas/v4",
)

# ================= 2. 构建 RAG 检索器 =================
loader = TextLoader(file_path="faq.txt", encoding="utf-8")
# 修复了原代码中 separator 的空字符串问题
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=10, separators=["\n\n", "\n", " ", ""]
)
vector_store = InMemoryVectorStore(embeddings)
vector_store.add_documents(text_splitter.split_documents(loader.load()))
retriever = vector_store.as_retriever()

# ================= 3. 定义动态路由逻辑 =================
# 用一个简单的 LLM 分类器来判断是否需要走 RAG
router_prompt = ChatPromptTemplate.from_template(
    "你是一个路由助手。请判断用户的问题是【日常闲聊】还是【具体业务问题】。\n"
    "如果是闲聊（如天气、打招呼），只输出单词：chat\n"
    "如果是业务问题（如公司规定、年假），只输出单词：rag\n"
    "用户问题：{question}"
)
router_chain = router_prompt | model | str_parser


def route_question(inputs):
    """根据 LLM 的输出决定路由分支"""
    question = inputs["question"]
    route = router_chain.invoke({"question": question}).strip().lower()
    return "rag" if "rag" in route else "chat"


# ================= 4. 构建不同的处理链 =================
# 4.1 闲聊链 (直接走大模型)
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的智能助理。"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])
chat_chain = chat_prompt | model | str_parser

# 4.2 RAG 链 (触发检索并拼接 Prompt)
rag_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个公司业务助理。请严格基于以下检索到的上下文回答问题：\n{context}"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])


def get_rag_context(inputs):
    """执行检索并格式化上下文"""
    docs = retriever.invoke(inputs["question"])
    return "\n\n".join([doc.page_content for doc in docs])


# 组装 RAG 链，使用 RunnablePassthrough.assign 将 context 注入到输入字典中
rag_chain = (
        RunnablePassthrough.assign(context=RunnableLambda(get_rag_context))
        | rag_prompt
        | model
        | str_parser
)

# 4.3 构建带路由的主链
# 路由判断逻辑返回 'rag' 或 'chat'，RunnableBranch 根据返回值分发
main_chain = RunnableBranch(
    (lambda x: route_question(x) == "rag", rag_chain),
    chat_chain  # 默认走闲聊链
)

# ================= 5. 加入长期记忆 (RunnableWithMessageHistory) =================
# 内存存储历史记录
store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# 包装主链，赋予记忆能力
conversation_chain = RunnableWithMessageHistory(
    main_chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

# ================= 6. 终端流式交互测试 =================
if __name__ == "__main__":
    session_id = "user_123"
    print("小助理已上线（输入 'exit' 退出）")

    while True:
        user_input = input("\n你: ")
        if user_input.lower() == 'exit':
            break

        print("小助理: ", end="", flush=True)

        # 使用 stream 实现打字机效果
        for chunk in conversation_chain.stream(
                {"question": user_input},
                config={"configurable": {"session_id": session_id}}
        ):
            # 配合 end="" 和 flush=True 实现流式打字机输出
            print(chunk, end="", flush=True)
        print()  # 换行