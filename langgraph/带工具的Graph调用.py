from typing import Literal

from langchain_core.messages import ToolMessage
from langchain_core.tools import tool
from langgraph.constants import END, START


@tool
def get_weather(city:str):
    """获取当地城市的天气"""
    weather_data={
        "北京":"晴天",
        "上海":"多云",
        "广州":"阴天",
        "深圳":"大雨",
        "杭州":"小雨"
    }
    return weather_data.get(city,"没有查询到天气")
@tool
def square_root(x:float):
    """计算平方根"""
    return x**0.5
tools=[get_weather,square_root]
tools_by_name={t.name:t for t in tools}
#准备模型
from langchain_deepseek import ChatDeepSeek
model=ChatDeepSeek(model="deepseek-chat",temperature=0.9)
#模型绑定工具
model_tools=model.bind_tools(tools)

"""
# 可以直接调用工具跳过模型的调用
r=model_tools.invoke("杭州和北京的天气如何")
print(r)
tool_call=r.tool_calls[0]
tool_name=tool_call['name']
tool_args=tool_call['args']
tool=tools_by_name[tool_name]
result=tool.invoke(tool_args)
"""
#写模型节点和工具节点
from langgraph.graph import StateGraph, MessagesState
def model_node(state:MessagesState):
    response =model_tools.invoke(state["messages"])
    return {"messages":[response]}
def tool_node(state:MessagesState):
    ai_message=state["messages"][-1]
    tool_calls=ai_message.tool_calls
    tool_messages=[]
    for tool_call in tool_calls:
        tool_name=tool_call["name"]
        tool_args=tool_call['args']
        tool=tools_by_name[tool_name]
        result=tool.invoke(tool_args)
        # 将工具的名字和唯一的id返回给模型,自动拼接到Toolmessages里
        """
        [
          {
            "content": "工具执行返回的具体内容字符串",
            "tool_call_id": "call_abc123", 
            "name": "工具的名称(可选，但强烈建议带上)",
            "type": "tool"
          }
        ]
        """
        tool_messages.append(ToolMessage(content=result,tool_call_id=tool_call["id"]))
    return {'messages':tool_messages}
#用调用模型后中是否包含了tool_call,如果有就进入工具节点，没有就直接进end
# 路由节点
def continue_node(state:MessagesState)->Literal["tool",END]:
    last_message=state["messages"][-1]
    # hasattr表示判断对象是否具有该属性
    if hasattr(last_message,"tool_calls")and last_message.tool_calls:
        return "tool"
    return END
builder=StateGraph(MessagesState)
builder.add_node("tool",tool_node)
builder.add_node('model',model_node)

builder.add_edge(START,"model")
builder.add_conditional_edges("model",continue_node)
builder.add_edge('tool','model')

Graph=builder.compile()

print(Graph.get_graph().draw_mermaid())
res=Graph.invoke({"messages":[{"role":"user","content":"北京的天气如何"}]})
print(res['messages'][-1].content)

