"""
将state的更新和下一个节点的名字放在一起
函数的返回值只能有一个，利用command将内容封装为一个对象
    update：用来指定要更新的state字段
    goto：用来指定下个节点
直接放弃router
"""
from langgraph.types import Command
from typing import TypedDict, Literal
from langgraph.graph import StateGraph
class ScoreState(TypedDict):
    score:int
    result:str
# 在这里标注返回类型，以实现和router一样的效果
def get_score(state:ScoreState)-> Command[Literal["success","fail"]]:
    score=int(input("请输入分数："))
    goto="fail"
    state["score"]=score
    if state["score"]>60:
        goto="success"
    return Command(
        goto=goto,
        update={"score":state["score"]}
    )
def success_node(state:ScoreState):
    return {"result":"success"}
def fail_node(state:ScoreState):
    return {"result":"fail"}
builder=StateGraph(ScoreState)
builder.add_node("score", get_score)
# 在这里不用去连接其他多个节点，让command自己去判断
builder.add_node("success", success_node)
builder.add_node("fail", fail_node)

from langgraph.constants import START,END
builder.add_edge(START, "score")
builder.add_edge("success", END)
builder.add_edge("fail", END)
Graph=builder.compile()

print(Graph.get_graph().draw_ascii())

res=Graph.invoke({})
print(res)