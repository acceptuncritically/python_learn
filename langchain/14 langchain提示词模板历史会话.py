"""
通过from_message方法，从列表中获取多轮次会话的模板
"""
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_deepseek import ChatDeepSeek

chat_prompt_template=ChatPromptTemplate.from_messages(
    [
        ("system","你是桑多涅，是情感聊天的人"),
        MessagesPlaceholder("history"),
        ("human","内容呢")
    ]
)
history_data=[
    ("human","帮助我消除负面情绪"),
    ("ai","你不用马上好起来，先让我陪你把这一分钟轻轻放下"),
    ("human","我们接下来干什么"),
    ("ai","接下来我们只做最小的一步：你选一个")
]
# prompt_text=chat_prompt_template.invoke({"history":history_data}).to_string()
model=ChatDeepSeek(model="deepseek-chat", temperature=0.7)
# 组成链，要求每一个组件都是Runnable接口的子类
chain=chat_prompt_template|model
#通过链去调用stream 和invoke
res=chain.invoke({"history":history_data})
print(res.content)
print("-"*30)
#通过stream流式输出
for chunk in chain.stream({"history":history_data}):
    print(chunk.content,end="",flush=True)