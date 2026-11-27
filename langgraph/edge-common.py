"""
普通边 add_edge(node_a,node_b)   固定流向ai执行完一定到b
    串行：整个工作流只有一条路径，路径中的节点按照顺序依次执行
    并行：整个工作流由多条路径，不同路径可以同时执行

条件边 add_condition_dege(node_a,router,mapping)     router的返回值决定下一节点ai执行完一定到b，但满足某个条件
"""
from typing import TypedDict, Annotated

def add(old,new) ->list:
    return old+new
class State(TypedDict):
    # 由于定义的node的类型为列表，在返回函数时要返回列表
    node: Annotated[list[str],add]
def node_a(state:State):
    state["node"]="a"
    print(f"a正在执行{state['node']}")
    return {"node":[state["node"]]}
def node_b(state:State):
    state["node"]="b"
    print(f"b正在执行{state['node']}")
    return {"node":[state["node"]]}
def node_c(state:State):
    state["node"]="c"
    print(f"c正在执行{state['node']}")
    return {"node":[state["node"]]}
def node_d(state:State):
    state["node"]="d"
    print(f"d正在执行{state['node'] }")
    return {"node":[state["node"]]}
from langgraph.graph import StateGraph
builder=StateGraph(State)
builder.add_node("a",node_a)
builder.add_node("b",node_b)
builder.add_node("c",node_c)
builder.add_node("d",node_d)
from langgraph.constants import START, END
builder.add_edge(START,"a")
builder.add_edge("a","b")
builder.add_edge("a","c")
builder.add_edge("b","d")
builder.add_edge("c","d")
builder.add_edge("d",END)

Graph=builder.compile()
# 不写会自动创建为空列表
print("--- 开始执行 ---")
# node更新内容时会根据节点的字典序生成顺序

# values是整个状态的快照，在并行节点完成内容并合并后才返回
# updates 是更新内容就会返回更新了什么内容
for event in Graph.stream({}, stream_mode="values"):
    # event 就是每次节点执行完后最新的完整 State
    print(f"当前节点列表: {event}")


