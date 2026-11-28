
from langchain_core.messages import HumanMessage, AIMessage
from langchain_deepseek import ChatDeepSeek
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, MessagesState

model=ChatDeepSeek(model="deepseek-chat",temperature=0.7)
config1={"configurable":{"thread_id":"t3"}}
config2={"configurable":{"thread_id":"t4"}}
def model_node(state:MessagesState):
    response=model.invoke(state["messages"])
    return {"messages":[response]}
builder=StateGraph(MessagesState)
builder.add_node("model",model_node)

from langgraph.constants import START, END
builder.add_edge(START,"model")
builder.add_edge("model",END)

Graph=builder.compile(checkpointer=InMemorySaver())
res=Graph.invoke({"messages":[HumanMessage(content="12个苹果分三个人，每个人多少个苹果")]},config1)
print(res["messages"][-1].content)
# 使用同一个thread_id 其中的历史会话记忆保存
print('-'*50)
res=Graph.invoke({"messages":[HumanMessage(content="那四个人分呢")]},config1)
print(res["messages"][-1].content)


res=Graph.invoke({"messages":[HumanMessage(content="那四个人分呢")]},config2)
print(res["messages"][-1].content)