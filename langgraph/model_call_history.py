from langchain_core.messages import HumanMessage, AIMessage
from langchain_deepseek import ChatDeepSeek
from langgraph.graph import StateGraph
from sympy.core import add

model=ChatDeepSeek(model="deepseek-chat",temperature=0.7)
from typing import TypedDict, Annotated


class ModelState(TypedDict):
    # input:HumanMessage
    # response:AIMessage
    # 将HumanMessage和AIMessage都放到一个list中
    messages:Annotated[list[HumanMessage | AIMessage], add]
def model_node(state:ModelState):
    # 入参要放list[Message]
    response=model.invoke(state["messages"])
    # 此时response是AIMessage
    return {"messages":[response]}
builder=StateGraph(ModelState)
builder.add_node("model",model_node)

from langgraph.constants import START, END
builder.add_edge(START,"model")
builder.add_edge("model",END)

Graph=builder.compile()
print(Graph.get_graph().draw_ascii())
res=Graph.invoke({"messages":[HumanMessage(content="hello")]})
print(res)





