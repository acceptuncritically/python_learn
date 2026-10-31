import os, json
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_deepseek import ChatDeepSeek


#message_to_dict 单个消息对象(BaseMessage类实例)-->字典
#messages_from_dict:[字典。字典...]->[消息，消息...]
#AIMessage HumanMessage SystemMessage 都是BaseMessage的子类

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self,session_id,storage_path):
        self.session_id=session_id
        self.storage_path=storage_path
        #完整的文件路径
        self.file_path=os.path.join(self.storage_path,self.session_id)
        #确保文件夹是存在的
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)
    def add_message(self, messages: list[BaseMessage]) -> None:
        all_messages=list(self.messages) #已有的消息列表
        all_messages.append(messages)   #新的和已有的合并为一个列表
        #将数据同步写入到本地文件中
        #类对象写入文件->一堆二进制
        #为了方便，可以将BaseMessage消息转为字典 借助json模块以json字符串写入文件
        #官方message_to_dict 单个消息对象->字典
        new_messages=[message_to_dict(message) for message in all_messages]
        with open(self.file_path, 'w',encoding='utf-8') as f:
            json.dump(new_messages, f, ensure_ascii=False, indent=2)
    @property
    def messages(self)->list[BaseMessage]:
        try:
            with open(self.file_path, 'r',encoding='utf-8') as f:
                messages_data=json.load(f)
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []
    def clear(self) -> None:
        with open(self.file_path,"w",encoding="utf-8") as f:
            json.dump([],f)
model=ChatDeepSeek(model="deepseek-chat",temperature=0.7)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
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
def get_history(session_id):
    return FileChatMessageHistory(session_id, "chat_history")
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
    print(conversation_chain.invoke({"input":"你就是喜欢哥伦比娅"},session_config))
    print(conversation_chain.invoke({"input":"你是谁,你喜欢谁"},session_config))