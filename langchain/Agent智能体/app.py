import time
import uuid

import streamlit as st
from agent.react_agent import ReactAgent


def new_agent():
    """新建 Agent = 新会话：同时换一个新的 thread_id（记忆按 thread_id 隔离）"""
    st.session_state["agent"] = ReactAgent()
    st.session_state["thread_id"] = "chat-" + uuid.uuid4().hex[:8]


st.set_page_config(page_title="机器人客服", page_icon="🤖")
st.title("机器人客服")
st.divider()

# 【历史记录】session_state 在页面 rerun 之间不会丢失：history 因此能保留下来
if "agent" not in st.session_state:
    new_agent()
if "message" not in st.session_state:
    st.session_state["message"] = []   # [{"role": "user"/"assistant", "content": "..."}]

# 侧边栏：会话信息 + 清空对话（只有用户主动点击时才刷新一次）
with st.sidebar:
    st.caption(f"会话 ID：{st.session_state['thread_id']}")
    if st.button("清空对话(press)", use_container_width=True):
        new_agent()
        st.session_state["message"] = []
        st.rerun()

# 【渲染历史记录】每次 rerun 都把之前的对话重新画出来
for message in st.session_state["message"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#用户输入提示词
prompt = st.chat_input()
if prompt:
    # 1) 用户消息：先写入历史并立即显示
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})

    # 2) 助手回复：思考过程放进 st.status，思考完成自动折叠
    with st.chat_message("assistant"):
        final_text = ""
        status = st.status("🤔 正在思考…", expanded=True)
        with status:
            events = st.session_state["agent"].execute_stream(
                prompt, thread_id=st.session_state["thread_id"]
            )
            for event in events:
                if event["type"] == "thinking":
                    st.markdown(f"🧠 **思考**：{event['content']}")
                elif event["type"] == "tool_call":
                    st.markdown(f"🛠 **行动**：调用工具 `{event['name']}`，入参 `{event['args']}`")
                elif event["type"] == "observation":
                    text = str(event["content"])
                    if len(text) > 400:
                        text = text[:400] + " ...(已截断)"
                    st.caption(f"👀 **观察**（{event['name']}）：{text}")
                elif event["type"] == "final":
                    final_text = event["content"]
                    break

        # 思考结束：自动折叠成一行（点击可展开），不再占用屏幕
        if final_text:
            status.update(label="思考完成（点击展开思考过程）", state="complete", expanded=False)
        else:
            final_text = "抱歉，本次没有生成有效回复，请换个问法重试。"
            status.update(label="⚠️ 思考完成，但未生成回复", state="error", expanded=False)

        # 3) 最终回答：保留原来的逐字打字机效果
        def typewriter(text, delay=0.01):
            for char in text:
                time.sleep(delay)
                yield char

        st.write_stream(typewriter(final_text))

    # 4) 回答写入历史（关键：不再 st.rerun()，靠 session_state 保留历史记录）
    st.session_state["message"].append({"role": "assistant", "content": final_text})