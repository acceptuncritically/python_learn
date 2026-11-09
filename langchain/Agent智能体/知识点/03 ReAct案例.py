from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek
from langchain_core.tools import tool

@tool(description="获取体重，返回一个整数 单位kg")
def get_weigh()->int:
    return 60
@tool(description="获取身高，返回整数身高，单位cm")
def get_high() -> int:
    return 179


agent = create_agent(
    model=ChatDeepSeek(model="deepseek-chat", temperature=0.9),
    tools=[get_high, get_weigh],
    system_prompt="你是一个严格遵循ReAct的智能助手，保证每次只能进行一轮思考和选择工具，"
                  "禁止同时调用多个工具,保证每轮只能调用一个工具"
                  "请告知我思考过程，让我知道你为什么调用某个工具"
)

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "我的BMI是多少"}]},
    stream_mode="values"
):
    latest_message = chunk['messages'][-1]

    if latest_message.content:
        print(type(latest_message).__name__, latest_message.content)

    try:
        if latest_message.tool_calls:
            print(f"工具调用：{[tc['name'] for tc in latest_message.tool_calls]}")
    except AttributeError as e:
        pass