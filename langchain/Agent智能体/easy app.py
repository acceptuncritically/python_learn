import time
import streamlit as st
from agent.react_agent import ReactAgent
st.title("机器人客服")
st.divider()
if "agent" not in st.session_state:
    st.session_state["agent"] = ReactAgent()
if "message" not in st.session_state:
    st.session_state["message"] = []
for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])
#用户输入提示词
prompt =st.chat_input()
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})
    response_messages=[]
    with st.spinner("智能客服思考中..."):
        res_stream=st.session_state["agent"].execute_stream(prompt)
        def capture(generator,cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                for char in chunk:      #使得像真流式输出
                    time.sleep(0.01)
                    yield char
        res = capture(res_stream, response_messages)
        st.chat_message("assistant").write(res)
        st.session_state["message"].append({"role": "assistant", "content": response_messages[-1]})
        st.rerun()
