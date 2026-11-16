"""
练习 3：ReAct 循环
目标：亲眼看到“模型自己决定先拿 ID、再查记录”的多轮工具调用，
      并理解这个循环是框架驱动的，提示词只是软约束。
运行：python main.py（需要环境变量 DEEPSEEK_API_KEY）
"""
import random

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek

print("=" * 60)
print("练习 3：ReAct 循环 —— 思考 -> 行动 -> 观察 -> 再思考")
print("=" * 60)


# 工具 ①：只能拿到“是谁”，拿不到记录内容
@tool(description="获取当前用户的ID，以纯字符串形式返回")
def get_user_id() -> str:
    return random.choice(["1001", "1002", "1003"])


# 工具 ②：必须传入 user_id 才能查记录 —— 这就强制模型先调用工具 ①
@tool(description="根据用户ID查询该用户最近一个月的扫地机器人使用记录，以字符串形式返回")
def get_user_record(user_id: str) -> str:
    return (
        f"用户{user_id}最近一个月：清洁面积 128㎡，清扫 46 次，"
        f"耗材（边刷）剩余 35%，较上月效率提升 8%"
    )


# system_prompt 是本课的“软约束”：要求严格 ReAct、每轮只调一个工具、先 ID 后记录
SYSTEM_PROMPT = (
    "你是一个严格遵循 ReAct 的智能助手，流程必须是：思考 -> 行动 -> 观察 -> 再思考。"
    "每一轮只能调用一个工具，禁止同时调用多个工具。"
    "如果要查用户使用记录，必须先调用 get_user_id 获取用户ID，"
    "再调用 get_user_record 查询记录；信息足够后再给出最终回答。"
    "调用工具前，先用一句中文说明你的思考。"
)

agent = create_agent(
    model=ChatDeepSeek(model="deepseek-chat", temperature=0.7),
    tools=[get_user_id, get_user_record],
    system_prompt=SYSTEM_PROMPT,
)

query = "帮我看看我最近一个月的扫地机器人使用记录，顺便给点保养建议"
print(f"\n用户提问：{query}")

# 用 values 模式逐帧看：每帧 = 完整快照，seen 保证只处理新增消息
seen = 0
round_no = 0
for frame, chunk in enumerate(
        agent.stream({"messages": [{"role": "user", "content": query}]},
                     stream_mode="values"), start=1):
    messages = chunk["messages"]
    if frame == 1:            # 第一帧只有用户消息，跳过
        seen = len(messages)
        continue
    for msg in messages[seen:]:
        if isinstance(msg, AIMessage):
            if msg.tool_calls:                    # 模型决定行动：打印思考 + 申请单
                round_no += 1
                print("\n" + "-" * 60)
                print(f"第 {round_no} 轮 | 思考：{msg.content or '（本次没有输出思考文本）'}")
                for tc in msg.tool_calls:
                    print(f"         行动：{tc['name']}  入参={tc['args']}")
            else:                                 # 没有申请单：最终回答
                print("\n" + "=" * 60)
                print("最终回答：", msg.content)
                print("=" * 60)
        elif isinstance(msg, ToolMessage):        # 工具执行结果：观察
            print(f"         观察：{msg.content}")
    seen = len(messages)

print(f"\n小结：这次一共发生了 {round_no} 轮工具调用。"
      "循环由框架驱动，不是模型在“跑循环”。")