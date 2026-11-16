"""
练习 1：造出你的第一个 Agent
目标：跑通 create_agent，并亲眼看到 messages 里的三种角色。
运行：python main.py（需要环境变量 DEEPSEEK_API_KEY）
"""
from langchain.agents import create_agent            # LangChain 1.x 的 Agent 组装入口
from langchain_core.messages import AIMessage        # 用来识别“模型说的话”
from langchain_core.tools import tool                # 把普通函数包装成 Agent 可调用的工具
from langchain_deepseek import ChatDeepSeek          # DeepSeek 聊天模型

print("=" * 60)
print("练习 1：最小 Agent —— 1 个工具 + 1 次 invoke")
print("=" * 60)


# ① 工具 = 普通 Python 函数 + @tool + description + 类型注解。
#    description 是写给“模型”看的说明书，模型靠它判断“要不要调用、传什么参数”。
@tool(description="获取指定城市的天气，以纯字符串形式返回")
def get_weather(city: str) -> str:
    """查询城市天气（本课写死数据，重点不是联网）。"""
    print(f"  >>> [工具真的在本地执行了] get_weather(city={city!r})")
    return f"城市{city}天气为晴天，气温26摄氏度，空气湿度50%，南风1级"


# ② 组装 Agent：模型 + 工具清单 + 系统提示词。
#    create_agent 内部会编译出一个“循环图”：模型 -> 工具 -> 模型 -> ... -> 结束。
model = ChatDeepSeek(model="deepseek-chat", temperature=0.7)
agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="你是天气助手，需要天气时调用工具",
)

# ③ 一次 invoke：入参是“本轮用户消息”，出参是“整段消息历史”（列表）。
res = agent.invoke({"messages": [{"role": "user", "content": "深圳今天天气怎么样"}]})

# ④ 逐条看消息历史 —— 这就是本课最重要的现象。
print("\n" + "=" * 60)
print(f"res['messages'] 里一共有 {len(res['messages'])} 条消息：")
print("=" * 60)
for i, msg in enumerate(res["messages"]):
    print(f"\n[{i}] {type(msg).__name__}")          # 类名就是消息角色
    print(f"    content = {msg.content!r}")         # 文本内容
    # 只有 AIMessage 才可能带 tool_calls：它是模型“申请调用工具”的原始数据
    if isinstance(msg, AIMessage) and msg.tool_calls:
        print(f"    tool_calls = {msg.tool_calls}")

# ⑤ 最后一条通常就是模型整合工具结果后给出的最终回答。
print("\n" + "=" * 60)
print("最终回答：", res["messages"][-1].content)
print("=" * 60)