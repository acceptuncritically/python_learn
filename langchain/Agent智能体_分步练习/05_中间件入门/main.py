"""第 05 课：中间件入门 —— 把 6 个钩子挂在 Agent 生命周期的 6 个位置。

运行重点：用户只说了一句话，但模型被调用了 2 次、工具被调用了 1 次，
所以不同钩子的触发次数并不一样。下面的时间线会给每次触发编号。
"""
from itertools import count

from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import (before_agent, after_agent, before_model,
                                        after_model, wrap_model_call, wrap_tool_call)
from langchain.tools.tool_node import ToolCallRequest
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek
from langgraph.runtime import Runtime

step = count(1)  # 全局计数器：给每次钩子触发编号，方便看谁先谁后


def show(name: str, detail: str) -> None:
    print(f"[{next(step):02d}] {name:<16}| {detail}")


@tool(description="查询指定城市的实时天气，返回一句天气描述")
def search_weather(city: str) -> str:
    """最简单的工具：固定返回晴天，不联网。"""
    print(f"       🛠  search_weather 真正执行：city={city!r}")
    return f"{city}今天晴，26℃，湿度 50%，适合扫地机器人工作"


@before_agent
def my_before_agent(state: AgentState, runtime: Runtime) -> None:
    # 整个 Agent 启动时执行（本次运行只 1 次）
    show("before_agent", f"Agent 启动，messages={len(state['messages'])} 条")


@after_agent
def my_after_agent(state: AgentState, runtime: Runtime) -> None:
    # 整个 Agent 结束时执行（本次运行只 1 次）
    show("after_agent", f"Agent 结束，messages={len(state['messages'])} 条")


@before_model
def my_before_model(state: AgentState, runtime: Runtime) -> None:
    # 每次“要调用模型之前”都执行
    show("before_model", f"马上调用模型，messages={len(state['messages'])} 条")


@after_model
def my_after_model(state: AgentState, runtime: Runtime) -> None:
    # 每次“模型返回之后”都执行，最后一条消息能看出模型想干嘛
    last = state["messages"][-1]
    show("after_model", f"模型刚返回，最后一条是 {type(last).__name__}")


@wrap_model_call
def my_wrap_model_call(request, handler):
    # “包住”一次模型调用：handler 前后各打印一次，形成 进入/退出 夹心
    show("wrap_model_call", "进入 —— 包住模型调用")
    response = handler(request)  # 这里才真正请求大模型
    show("wrap_model_call", "退出 —— 模型已返回")
    return response


@wrap_tool_call
def my_wrap_tool_call(request: ToolCallRequest, handler) -> ToolMessage:
    # “包住”一次工具调用：从 request.tool_call 拿得到工具名和参数
    show("wrap_tool_call", f"进入 —— 工具={request.tool_call['name']} 参数={request.tool_call['args']}")
    result = handler(request)  # 这里才真正执行工具函数
    show("wrap_tool_call", f"退出 —— 工具返回 {str(result.content)[:30]}")
    return result


# 6 个钩子全部注册进 middleware 列表
agent = create_agent(
    model=ChatDeepSeek(model="deepseek-chat", temperature=0.9),
    tools=[search_weather],
    middleware=[my_before_agent, my_after_agent, my_before_model,
                my_after_model, my_wrap_model_call, my_wrap_tool_call],
)

print("=" * 60)
print("👤 用户：深圳今天天气怎么样？")
print("=" * 60)
res = agent.invoke({"messages": [{"role": "user", "content": "深圳今天天气怎么样？"}]})
print("=" * 60)
print("🤖 最终回答：", res["messages"][-1].content)
print("=" * 60)