from langchain_core.messages import HumanMessage, AIMessage
from langchain_deepseek import ChatDeepSeek
from langgraph.graph import StateGraph
from sympy.core import add

model=ChatDeepSeek(model="deepseek-chat",temperature=0.7)
from typing import TypedDict, Annotated

# 在真实使用时可以直接继承MessageState
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
# res=Graph.invoke({"messages":[HumanMessage(content="hello")]})
# print(res)

"""
stream_events(version="v3")：适用于大多数正式项目，尤其是前端或复杂 Agent 应用。
它让你从 if/elif 的分支判断中解放出来，通过 stream.messages、stream.tool_calls 等直观的属性，
就能优雅地消费结构化的流式数据。你的代码示例正是其典型用法：
直接迭代 stream.messages，再消费 message.text 获取纯文本增量。
"""
stream=Graph.stream_events({"messages":[HumanMessage(content="hello")]},version="v3")
for message in stream.messages:
    for chunk in message.text:
        print(chunk, end="", flush=True)

"""
Graph.stream()：适用于快速原型、简单场景，或者你完全清楚如何处理原始事件流，喜欢手动控制的感觉。
"""
# for chunk in Graph.stream({"messages":[HumanMessage(content="hello")]}):
#     print(chunk["model"]["messages"][0].content, end="", flush=True)



