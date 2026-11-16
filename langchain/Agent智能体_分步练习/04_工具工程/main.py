"""
练习 4：工具工程
目标：搞清 @tool 的工具是怎么“写给模型看”的：函数名 + 描述 + 参数类型注解；
      以及返回值为什么必须统一成字符串、异常为什么要自己兜住。
运行：python main.py（需要环境变量 DEEPSEEK_API_KEY）
"""
import csv
import os
import random

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek

print("=" * 60)
print("练习 4：工具工程 —— 描述、类型注解、返回值契约")
print("=" * 60)


# 工具 ①：描述里写清“参数是什么、返回什么”，模型才知道什么时候该用
@tool(description="获取指定城市的天气，以纯字符串形式返回")
def get_weather(city: str) -> str:
    return f"城市{city}天气为晴天，气温26摄氏度，空气湿度50%"


# 工具 ②：无入参。没有类型注解的参数，模型也没法给你瞎编
@tool(description="获取当前用户的ID，以纯字符串形式返回")
def get_user_id() -> str:
    return random.choice(["1001", "1002", "1003"])


# 以 main.py 所在目录为基准拼数据路径：不管从哪个目录启动都能找到 csv
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "records.csv")


# 工具 ③：真读文件。参数注解 str 会变成给模型看的参数说明；
#         命中/未命中/出错都返回 str —— 统一返回值类型，模型才好理解。
@tool(description="根据用户ID和月份（格式 YYYY-MM，如 2025-06）查询扫地机器人使用记录，返回格式化字符串")
def query_record(user_id: str, month: str) -> str:
    try:
        with open(DATA_PATH, "r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                if row["user_id"] == user_id and row["month"] == month:
                    return (f"用户{user_id} {month} 使用记录："
                            f"特征={row['feature']}；效率={row['efficiency']}；"
                            f"耗材={row['consumable']}；对比={row['comparison']}")
        return f"未查询到用户{user_id}在{month}的使用记录"
    except Exception as e:          # 文件缺失、格式异常等，绝不让异常抛给框架
        return f"查询失败，请检查 data/records.csv：{e}"


agent = create_agent(
    model=ChatDeepSeek(model="deepseek-chat", temperature=0.7),
    tools=[get_weather, get_user_id, query_record],
    system_prompt=(
        "你是扫地机器人客服。用户要查使用记录时调用 query_record；"
        "问题里已经给出用户ID和月份就直接查询，不要调用其它工具。"
        "请如实转述工具返回的内容，不要编造数据。"
    ),
)

# 一问命中、一问未命中：亲眼看到两种返回值都能被模型接住
questions = [
    "帮我查一下用户 1001 在 2025-06 的使用记录",
    "帮我查一下用户 1001 在 2024-01 的使用记录",
]
for q in questions:
    print("\n" + "=" * 60)
    print("用户提问：", q)
    res = agent.invoke({"messages": [{"role": "user", "content": q}]})
    for msg in res["messages"]:
        if isinstance(msg, AIMessage) and msg.tool_calls:
            for tc in msg.tool_calls:
                print(f"🛠 模型申请调用：{tc['name']}  入参={tc['args']}")
        elif isinstance(msg, ToolMessage):
            # 打印 type：验证工具返回值最终以什么类型回到模型上下文里
            print(f"👀 {msg.name} 返回（type={type(msg.content).__name__}）：{msg.content}")
    print("最终回答：", res["messages"][-1].content)

print("\n" + "=" * 60)
print("工具工程的三个要点：描述清楚 + 类型注解准确 + 返回值统一 str 且兜住异常")
print("=" * 60)