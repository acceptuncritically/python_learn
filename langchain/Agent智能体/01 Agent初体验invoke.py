from langchain_deepseek import ChatDeepSeek
from langchain.agents import create_agent
from langchain_core.tools import tool

@tool(description="获取天气情况")
def get_weather():
    return "晴天"
model=ChatDeepSeek(model="deepseek-chat",temperature=0.9)
agent=create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="你是一个有天气查询功能的助手"
)
res=agent.invoke(
    {"messages":[
        {"role":"user","content":"今天天气如何"}
    ]
})
print(res["messages"])

for msg in res["messages"]:
    print(type(msg).__name__, msg.content)
