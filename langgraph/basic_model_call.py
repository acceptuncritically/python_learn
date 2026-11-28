from langchain_deepseek import ChatDeepSeek
from langgraph.graph import StateGraph

model=ChatDeepSeek(model="deepseek-chat",temperature=0.7)
# 创建state
from typing import TypedDict
class ModelState(TypedDict):
    input:str
    response:str
def model_node(state:ModelState):
    """
    返回AImessage，调用model和agent不同
    入参
    -model str|list[BaseMessage]
    -agent dict dict里有message 第一条消息列表list[BaseMessage]
    返回值
    -model AIMessage
    """
    response=model.invoke(state["input"])
    return {"response":response.text}
builder=StateGraph(ModelState)
builder.add_node("model",model_node)

from langgraph.constants import START, END
builder.add_edge(START,"model")
builder.add_edge("model",END)

Graph=builder.compile()
print(Graph.get_graph().draw_ascii())
res=Graph.invoke({"input":"hello"})
print(res)





