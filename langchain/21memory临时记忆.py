"""
如果想要封装历史记录，除了自行维护历史消息外，也可以借助LangChain内置的历史记录附加功能。
LangChain提供了History功能，帮助模型在有历史记忆的情况下回答。
  • 基于RunnableWithMessageHistory在原有链的基础上创建带有历史记录功能的新链（新Runnable实例）
  • 基于InMemoryChatMessageHistory为历史记录提供内存存储（临时用）

from langchain_core.runnables.history import RunnableWithMessageHistory

# 通过RunnableWithMessageHistory获取一个新的带有历史记录功能的chain
conversation_chain = RunnableWithMessageHistory(
    some_chain,                  # 被附加历史消息的Runnable，通常是chain
    None,                        # 获取指定会话ID的历史会话的函数
    input_messages_key="input",  # 声明用户输入消息在模板中的占位符
    history_messages_key="chat_history" # 声明历史消息在模板中的占位符
)

# 获取指定会话ID的历史会话记录函数
chat_history_store = {}      # 存放多个会话ID所对应的历史会话记录
# 函数传入为会话ID（字符串类型）
# 函数要求返回BaseChatMessageHistory的子类
# BaseChatMessageHistory类专用于存放某个会话的历史记录
# InMemoryChatMessageHistory是官方自带的基于内存存放历史记录的类
def get_history(session_id):
    if session_id not in chat_history_store:
        # 返回一个新的实例
        chat_history_store[session_id] = InMemoryChatMessageHistory()
    return chat_history_store[session_id]
"""
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_deepseek import ChatDeepSeek
from langchain_core.runnables.history import RunnableWithMessageHistory
# from langchain_core.prompts import PromptTemplate# 注释掉或删除这行
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

model=ChatDeepSeek(model="deepseek-chat",temperature=0.7)
str_parser=StrOutputParser()

# prompt=ChatPromptTemplate.from_messages(
#     "请根据历史会话信息{chat_history}我的问题{input}，给出详细的回答。"
# )

prompt = ChatPromptTemplate.from_messages([
    ("system", "请根据历史会话信息，给出详细的回答。"),
    MessagesPlaceholder(variable_name="chat_history"), # 关键点：将历史记录作为消息列表插入
    ("human", "{input}")
])
chain=prompt| model | str_parser
dict1={}
def get_history(session_id):
    if session_id not in dict1:
        dict1[session_id] = InMemoryChatMessageHistory()
    return dict1[session_id]
conversation_chain = RunnableWithMessageHistory(
    chain,                  # 被附加历史消息的Runnable，通常是chain
    get_history,                        # 获取指定会话ID的历史会话的函数
    input_messages_key="input",  # 声明用户输入消息在模板中的占位符
    history_messages_key="chat_history" # 声明历史消息在模板中的占位符
)
if __name__ == "__main__":
    # 固定格式添加langchain的配置 为当前程序配置所属的session_id
    session_config={
        "configurable":{
            "session_id": "test_session_id"
        }
    }

    print(conversation_chain.invoke({"input":"你是桑多涅"},session_config))
    print(conversation_chain.invoke({"input":"你喜欢哥伦比亚"},session_config))
    print(conversation_chain.invoke({"input":"你是谁,你喜欢谁"},session_config))

