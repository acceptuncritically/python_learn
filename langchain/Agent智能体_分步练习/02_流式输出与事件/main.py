"""
练习 2：流式输出与事件
目标：用 stream(stream_mode="values") 看“每一步的完整快照”，
      并把新增消息翻译成人能看懂的 4 类事件。
运行：python main.py（需要环境变量 DEEPSEEK_API_KEY）
"""
from langchain.agents import create_agent
from langchain_core.messages import AIMessage, ToolMessage   # 用来给新增消息分类
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek

print("=" * 60)
print("练习 2：stream(stream_mode='values') —— 快照不是增量")
print("=" * 60)


# 两个工具：一个问题里可能两个都被调用，方便观察多轮/并行
@tool(description="获取股票当前价格，传入股票名称，返回字符串")
def get_price(name: str) -> str:
    return f"股票{name}的价格是20元"


@tool(description="获取股票公司简介，传入股票名称，返回字符串")
def get_info(name: str) -> str:
    return f"股票{name}，是一家A股上市公司"


agent = create_agent(
    model=ChatDeepSeek(model="deepseek-chat", temperature=0.7),
    tools=[get_price, get_info],
    system_prompt="你是股票助手。需要价格或简介时调用工具，请先说明你的思考过程。",
)

query = "deepseek股价多少，并简单介绍一下这家公司"
print(f"\n用户提问：{query}")

# seen 记录“已经处理过的消息条数”：快照会重复包含旧消息，靠它只处理新增部分
seen = 0
frame = 0
for chunk in agent.stream({"messages": [{"role": "user", "content": query}]},
                          stream_mode="values"):
    # stream_mode = "values"
    # 相当于告诉流水线：“每经过一个节点加工（或者每当状态发生变化），就把当前完整的整体状态给我截个图。”
    frame += 1
    messages = chunk["messages"]      # 注意：这是“到目前为止的完整快照”，不是增量
    print("\n" + "-" * 60)
    print(f"第 {frame} 帧 | len(messages)={len(messages)} | "
          f"类型={[type(m).__name__ for m in messages]}")

    if frame == 1:
        # 没有 checkpointer 时，第一帧只有本轮用户消息（HumanMessage）
        # 此时 frame==1 跳过，避免把“用户提问”重复输出成一次事件
        seen = len(messages)
        # print(seen,messages)
        continue

    for msg in messages[seen:]:       # 切片：只看这一帧新增的消息
        # LangGraph是按照节点（Node）来执行的，每一帧快照对应的是某一个节点刚刚执行完毕的状态。
        # 绝对不会出现一个节点中同时出现ToolMessage和AIMessage两个消息对象
        print(f"messages[seen:]:{messages[seen:]} msg: {msg}")
        if isinstance(msg, AIMessage):
            if msg.tool_calls:        # 有申请单：先 thinking 文本，再逐个 tool_call
                if msg.content:
                    print(f"🧠 thinking    : {msg.content}")
                for tc in msg.tool_calls:
                    print(f"🛠  tool_call   : {tc['name']}  args={tc['args']}")
            elif msg.content:         # 没有申请单、但有文本：最终回答
                print(f"final       : {msg.content}")
        elif isinstance(msg, ToolMessage):   # 工具返回：观察
            print(f"👀 observation : {msg.name} -> {msg.content}")
    seen = len(messages)              # 更新游标：这些消息下次不再处理

print("\n" + "=" * 60)
print("流结束：tool_call 和 observation 各出现几次，就是发生了几轮“行动 + 观察”")
print("=" * 60)