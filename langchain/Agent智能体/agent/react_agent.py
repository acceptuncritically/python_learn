from langchain.agents import create_agent
from langchain_core.messages import AIMessage, ToolMessage
from langgraph.checkpoint.memory import InMemorySaver

from model.factory import chat_model
from main.prompt_loader import load_system_prompts
from agent.tools.agent_tools import (rag_summarize,get_weather,
get_user_id,get_user_location,get_current_month,
fetch_external_data,fill_context_for_report)
from agent.tools.middleware import monitor_tool, log_before_model, report_prompt_switch
class ReactAgent:
    def __init__(self):
        # 【新增】记忆组件：checkpointer 负责按 thread_id 保存/恢复对话历史。
        # 主流程不变，只是给 create_agent 多传一个 checkpointer 参数。
        self.checkpointer = InMemorySaver()
        self.agent=create_agent(
            model=chat_model,
            system_prompt=load_system_prompts(),
            tools=[rag_summarize,get_weather,
get_user_id,get_user_location,get_current_month,
fetch_external_data,fill_context_for_report],
        middleware=[monitor_tool, log_before_model, report_prompt_switch],
        checkpointer=self.checkpointer,   # ← 开启多轮记忆
        )
    def execute_stream(self,query:str,thread_id:str="default"):
        """流式执行一次提问，产出结构化事件，方便前端区分“思考”和“回答”。

        产出的事件（dict）：
          {"type": "thinking",    "content": "..."}            模型的思考/中间文本
          {"type": "tool_call",   "name": "...", "args": {}}   发起工具调用（行动）
          {"type": "observation", "name": "...", "content": "..."} 工具返回（观察）
          {"type": "final",       "content": "..."}            最终回答
        """
        input_dict={
            "messages": [
                {"role": "user","content": query}
            ]
        }
        # thread_id 相当于会话 ID：同一个 thread_id 会自动带上历史消息（多轮记忆）
        config={"configurable":{"thread_id":thread_id}}
        seen = None
        #第三个参数context就是上下文runtime中的信息 就是我们做提示词切换的标记
        for chunk in self.agent.stream(input_dict,stream_mode="values",config=config,context={"report": False}):
            messages = chunk["messages"]
            if seen is None:
                # 第一帧 = 历史消息 + 本轮用户消息，跳过，避免把历史重复输出
                seen = len(messages)
                continue
            for message in messages[seen:]:
                if isinstance(message, AIMessage):
                    if message.tool_calls:                      # 有工具调用：先思考后行动
                        if message.content:
                            yield {"type": "thinking", "content": message.content}
                        for tool_call in message.tool_calls:
                            yield {
                                "type": "tool_call",
                                "name": tool_call["name"],
                                "args": tool_call.get("args", {}),
                            }
                    elif message.content:                       # 无工具调用：最终回答
                        yield {"type": "final", "content": message.content}
                elif isinstance(message, ToolMessage):          # 工具返回：观察
                    yield {
                        "type": "observation",
                        "name": message.name,
                        "content": str(message.content),
                    }
            seen = len(messages)
if __name__ == "__main__":
    agent = ReactAgent()
    for event in agent.execute_stream("扫地机器人如何保养", thread_id="cli-demo"):
        if event["type"] == "thinking":
            print(f"\n🧠 思考：{event['content']}")
        elif event["type"] == "tool_call":
            print(f"\n🛠  行动：调用工具 {event['name']}，入参 {event['args']}")
        elif event["type"] == "observation":
            print(f"\n👀 观察：{event['content'][:200]}")
        elif event["type"] == "final":
            print(f"\n✅ 最终回答：{event['content']}")