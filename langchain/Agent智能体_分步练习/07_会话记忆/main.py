"""第 07 课：会话记忆 —— InMemorySaver + thread_id，让 Agent 记住上一轮说过的内容。"""
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek
from langgraph.checkpoint.memory import InMemorySaver


@tool(description="查询指定城市今天的天气")
def get_weather(city: str) -> str:
    return f"{city}今天晴，26℃"


def build_agent(checkpointer=None):
    """checkpointer=None 表示不存历史；传入 InMemorySaver() 表示按 thread_id 存历史。"""
    return create_agent(
        model=ChatDeepSeek(model="deepseek-chat", temperature=0.3),
        tools=[get_weather],
        system_prompt="你是扫地机器人客服助手，回答简短，最多两句话。",
        checkpointer=checkpointer,
    )


def ask(agent, question, thread_id=None):
    """同一个 thread_id 再问一次，模型才能看到上一轮的对话历史。"""
    config = {"configurable": {"thread_id": thread_id}} if thread_id else None
    result = agent.invoke({"messages": [{"role": "user", "content": question}]}, config=config)
    print(f"👤 {question}")
    print(f"🤖 {result['messages'][-1].content}\n")


print("=" * 60)
print("实验一：一个 InMemorySaver + 同一个 thread_id 连问 3 轮")
print("=" * 60)
memory = InMemorySaver()
agent_mem = build_agent(memory)  # 装上记忆组件

# 3 轮都传同一个 thread_id="chat-001"，历史会自动接上
ask(agent_mem, "记住：我叫小明。", "chat-001")
ask(agent_mem, "我叫什么？", "chat-001")
ask(agent_mem, "我刚才说了什么？", "chat-001")

# 打开这个会话的存档看看：历史真的被 checkpointer 存下来了
snapshot = agent_mem.get_state({"configurable": {"thread_id": "chat-001"}})
print(f"🗂  thread_id=chat-001 的存档里有 {len(snapshot.values['messages'])} 条消息\n")

print("=" * 60)
print("实验二：换成 thread_id=chat-002，同一个 Agent 还认识我吗？")
print("=" * 60)
ask(agent_mem, "我叫什么？", "chat-002")

print("=" * 60)
print("实验三：不带 checkpointer 的 Agent，第二轮会怎样？")
print("=" * 60)
agent_no_mem = build_agent()  # checkpointer=None，等于完全没有记忆
ask(agent_no_mem, "记住：我叫小红。")
ask(agent_no_mem, "我叫什么？")
print("=" * 60)
print("结论：记忆不属于 Agent 对象，而属于 InMemorySaver 里以 thread_id 为键的存档。")
print("=" * 60)