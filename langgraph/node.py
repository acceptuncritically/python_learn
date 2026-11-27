# 1 state
# 2 node
# 3 edge
from typing import TypedDict

from langgraph.constants import START, END
from langgraph.graph import StateGraph
# 1定义state
"""
通过继承typeddict 将state定义为一个类，但实际为一个字典，通过定义类中的变量
来保证字典中的key 不会混乱，返回的也是一个字典 
"""
class State(TypedDict):
    name:str
    greeting:str
# 2 创建node
def first_node(state:State):
    name=state.get("name")
    greeting=f"hello {name}"
    print(f"first_node正在执行，接收到{name}")
    return {"greeting":greeting}
def second_node(state:State):
    greeting=state.get("greeting").upper()
    print(f"second_node正在执行,接收到{greeting}")
    return {"greeting":greeting}
# 3连接边
builder =StateGraph(State)          #通过stategraph生成一个图builder
# 添加节点时将节点名，和节点值同时传入
builder.add_node("first_node",first_node)# 把节点加入graph
builder.add_node("second_node",second_node)

# 将节点连接
# 第一个节点和第二个节点进行连接
builder.add_edge(START,"first_node")
builder.add_edge("first_node","second_node")
builder.add_edge("second_node",END)

# 此时生成了一个 start->first_node->second_node->end的图
graph=builder.compile()
result=graph.invoke({"name":"lu"})
print(result)