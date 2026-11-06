import streamlit as st
from knowledge_base import KnowledgeBase
import time

st.title("知识库更新")
# ❌ 原代码 type 里包含 pdf/doc/docx，但下面统一用
#    uploader.getvalue().decode("utf-8") 读内容，二进制文件会直接抛 UnicodeDecodeError。
# ✅ 修正：当前 unload_by_str 只接收字符串，先只开放 txt；
#    以后要支持 pdf/docx，需要先用 PyPDFLoader / Docx2txtLoader 提取文本再入库。
uploader = st.file_uploader(
    "上传文件",
    type=["txt"],
    accept_multiple_files=False,  # 保证不能够同时上传多个文件
)

if "count" not in st.session_state:
    st.session_state["count"] = KnowledgeBase()

if uploader is not None:
    file_size = uploader.size / 1024
    file_type = uploader.type
    st.subheader("文件信息")
    st.write(f"文件类型：{file_type},文件大小：{file_size:.2f} kB")
    content = uploader.getvalue().decode("utf-8")
    st.write(f"文件内容：{content}")
    with st.spinner("上传中..."):
        time.sleep(2)
        res = st.session_state["count"].unload_by_str(content, uploader.name)
        st.write(res)
