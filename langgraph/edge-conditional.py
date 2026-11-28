"""
接收三个参数：
    node_a:当前节点（这条边开始）
    router：路由函数，逻辑自定义，他的返回值默认就是下个节点的名字
    mapping：如果router返回值与下个节点名不一样，可以用mapping定义返回值与下个节点名字的映射关系
演示示例：
    start-> get_score ->success_node->end
                    |-> fail_node- >|
"""
from typing import TypedDict, Literal
from IPython.display import Image


class ScoreState(TypedDict):
    score: int
    result: str
def get_score(state: ScoreState) -> dict:
    score=input("请输入分数：")
    return {"score":int(score)}
def success_node(state: ScoreState) -> dict:
    return {"result":"success"}
def fail_node(state: ScoreState) -> dict:
    return {"result":"fail"}
# 要指定返回的类型，用于让其知道节点是如何连接的
def my_router(state:ScoreState)->Literal["success_node", "fail_node"]:
    score=state["score"]
    if score>=60:
        return "success_node"
    else:
        return "fail_node"
from langgraph.graph import StateGraph
builder=StateGraph(ScoreState)
builder.add_node("get_score", get_score)
builder.add_node("success_node", success_node)
builder.add_node("fail_node", fail_node)

from langgraph.constants import START,END
builder.add_edge(START,"get_score")
builder.add_conditional_edges("get_score",my_router )
builder.add_edge("success_node",END)
builder.add_edge("fail_node",END)

Graph=builder.compile()
# print(Image(Graph.get_graph(xray=True).draw_mermaid_png()))


# 生成节点图
print(Graph.get_graph().draw_ascii())


"""
LangGraph 的输入要求为状态字典（例如 {"messages": []}）。
    如果传递了普通的字符串如 Graph.invoke("test") 或 Graph.stream("test", stream_mode="values")，
    由于内部机制将其按可迭代对象展开或存放，打印时就会变成 't'、'e'、's'、't'。
不能使用values模式：langGraph 要求每个节点函数必须返回字典。
    如果节点内部直接写了 return "success" 或返回了字符串，
    框架无法将字符串与状态字段对应，打印时同样会降级为字符序列。
"""
res=Graph.invoke({})
print(res)

