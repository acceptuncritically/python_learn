# 在langgraph中，state的默认reducer采用覆盖策略，即后一个state会覆盖前一个state
# 可以通过自定义reducer来实现其想要的功能：将下一个state和上一个state进行合并
# 来定义
# Annotated[type,reducer]
from typing import TypedDict, Annotated

from langgraph.constants import START, END
from langgraph.graph import StateGraph
def add(old,new):
    return old+new

class State(TypedDict):
    # 由于count没有添加reducer，nodes有reducer
    # count是覆盖替换，nodes是累计添加
    count:int
    nodes:Annotated[list[str],add]
def node1(state:State):
    new_count=state["count"]=1
    print(f"node1 已拿到{state}")
    state["nodes"]="node1"
    print(f"node1 已经更新{state}")
    return {"count":new_count,"nodes":[state["nodes"]]}
def node2(state:State):
    new_count=state["count"]=2
    print(f"node2 已拿到{state}")
    state["nodes"]="node2"
    print(f"node2 已经更新{state}")
    return {"count":new_count,"nodes":[state["nodes"]]}
builder =StateGraph(State)
builder.add_node("1",node1)
builder.add_node("2",node2)
builder.add_edge(START,"1")
builder.add_edge("1","2")
builder.add_edge("2",END)
Graph=builder.compile()
res=Graph.invoke({"count":0,"nodes":[]})
print(res)