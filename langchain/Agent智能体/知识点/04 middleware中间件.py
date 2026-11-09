"""     可以插入的位置
1.Agent执行前
2.Agent执行后
3.model执行前
4.model执行后
5.工具执行中
6.模型执行中
"""
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, wrap_model_call, \
    wrap_tool_call
from langchain_deepseek import ChatDeepSeek
from langchain.agents import create_agent, AgentState
from langchain_core.tools import tool
from langgraph.runtime import Runtime

@tool(description="搜索城市天气")
def search(city: str) -> str:
    return "晴天"
@before_agent
def log_before_agent(state:AgentState,runtime:Runtime)->None:
    #agent执行前会调用这个函数并传入state和runtime两个对象
    print(f"[before_agent]agent启动，并附带{len(state["messages"])}消息")
@after_agent
def log_after_agent(state:AgentState,runtime:Runtime)->None:
    print(f"[after_agent]agent启动，并附带{len(state["messages"])}消息")
@before_model
def log_before_model(state:AgentState,runtime:Runtime)->None:
    print(f"[before_model]model启动，并附带{len(state["messages"])}消息")
@after_model
def log_after_model(state:AgentState,runtime:Runtime)->None:
    print(f"[after_model]model启动，并附带{len(state["messages"])}消息")
@wrap_model_call
def model_call_hook(request,handler):
    print("模型调用")
    return handler(request)
@wrap_tool_call
def monitor_tool(request,handler):
    print(f"工具调用{request.tool_call["name"]}")
    print(f"工具执行传入参数{request.tool_call["args"]}")
    return handler(request)
agent=create_agent(
    tools=[search],
    model=ChatDeepSeek(model="deepseek-chat",temperature=0.9),
    middleware=[log_before_agent,log_after_agent,log_before_model,log_after_model,monitor_tool,model_call_hook]
)
res=agent.invoke({"messages":[{"role":"user","content":"深圳今天天气怎么样"}]})
print(res["messages"][-1].content)

