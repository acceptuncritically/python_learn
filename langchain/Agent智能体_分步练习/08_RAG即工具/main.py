"""
第 08 关：RAG 即工具 —— 把「检索 + 总结」包成一个 @tool
============================================================
本文件里有两条互相独立的线，先看清这一点再读代码：

  建库线（离线，数据变了才跑）：
    data/*.txt --TextLoader--> 文档 --切块--> 小段文本 --智谱 embedding--> Chroma 落盘

  查询线（在线，每次提问都跑）：
    问题 --retriever(k=3)--> 3 段原文 --拼进提示词--> DeepSeek --> 摘要

最后把查询线包成 @tool 交给 Agent：Agent 只需要一句人话 query，
检索和总结都藏在工具内部，Agent 拿到的是干净摘要。

运行：cd 到本文件夹，然后 & $py main.py
"""

import glob
import os

from langchain.agents import create_agent
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ---------- 0. 路径：全部基于本文件所在目录，和你在哪个目录运行无关 ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CHROMA_DIR = os.path.join(BASE_DIR, "chroma_db")

# 查询线要用的两个对象，在 main() 里初始化（由建库线返回的向量库派生出来）
retriever = None
rag_chain = None

# 查询线用的提示词：把「用户问题 + 检索到的参考资料」拼成一段话
RAG_PROMPT = PromptTemplate.from_template(
    "你是一名扫地机器人选购与保养顾问。\n"
    "请严格根据下面的参考资料回答问题，资料里没写的内容不要编造。\n\n"
    "问题：{input}\n\n"
    "参考资料：\n{context}\n\n"
    "请用 3~5 句中文给出结论和理由。"
)


# ---------- 1. 建库线：离线跑，数据变了才需要重建 ----------
def build_store() -> Chroma:
    """读 data/ 下的 txt，切块、算向量，存进本文件夹的 chroma_db。"""
    print("=" * 60)
    print("① 建库线：检查向量库里有没有数据")

    vs = Chroma(
        collection_name="practice",  # 类似"表名"，同一个库里可以放多个集合
        embedding_function=ZhipuAIEmbeddings(
            model="embedding-3",  # 智谱的向量模型，把文字变成一串数字
            api_key=os.getenv("ZHIPU_API_KEY"),
        ),
        persist_directory=CHROMA_DIR,  # 绝对路径，保证落盘位置固定
    )

    # 先看库里已有多少条；有就跳过，避免每次运行都重复花钱算 embedding
    existing_ids = vs.get()["ids"]
    if existing_ids:
        print(f"已存在 {len(existing_ids)} 条，跳过建库")
        return vs

    # 1) 读文件：每个 txt 变成 Document（page_content 是正文）
    documents = []
    for txt_path in sorted(glob.glob(os.path.join(DATA_DIR, "*.txt"))):
        documents.extend(TextLoader(txt_path, encoding="utf-8").load())
    print(f"📄 读到 {len(documents)} 个文本文件")

    # 2) 切块：一篇长文切成 200 字左右的小段，相邻段重叠 20 字防止句子被切断
    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    chunks = splitter.split_documents(documents)
    print(f"✂️  切成 {len(chunks)} 块（chunk_size=200，chunk_overlap=20）")

    # 3) 存库：add_documents 会调用 embedding 模型，把每块变成向量后写入 Chroma
    vs.add_documents(chunks)
    print(f"✅ 建库完成：{len(chunks)} 条已写入 {CHROMA_DIR}")
    return vs


# ---------- 2. 查询线：每次提问都跑，检索 3 段再让模型总结 ----------
def rag_summarize_impl(query: str) -> str:
    """输入一句问题，检索最相关的 3 段资料，交给大模型总结成一段话。"""
    # retriever.invoke 返回 Document 列表（默认按相似度排序）
    docs = retriever.invoke(query)
    print(f"🔍 检索到 {len(docs)} 段资料，拼进提示词后交给模型总结")

    context = ""
    for i, doc in enumerate(docs, start=1):
        context += f"参考消息{i}:{doc.page_content}\n\n"

    # 这就是第 01 关学过的「提示词 | 模型 | 解析器」链，只是输入里多了 context
    return rag_chain.invoke({"input": query, "context": context})


# ---------- 3. RAG 即工具：把查询线包成 @tool 交给 Agent ----------
@tool(description="从知识库检索扫地机器人的选购、使用、保养资料，输入一句中文问题，返回一段总结后的专业参考")
def rag_summarize(query: str) -> str:
    """Agent 只负责给出人话 query；检索、拼参考资料、总结都在这个工具内部完成。"""
    print(f"\n🔧 [工具被调用] rag_summarize(query={query!r})")
    return rag_summarize_impl(query)


def main():
    global retriever, rag_chain

    # 第一步：建库线（第二次运行会打印"跳过建库"）
    vs = build_store()

    # 第二步：查询线用到的两个对象——检索器 + 大模型链
    print("=" * 60)
    print("② 查询线：准备检索器（k=3）和大模型链")
    retriever = vs.as_retriever(search_kwargs={"k": 3})
    rag_chain = RAG_PROMPT | ChatDeepSeek(model="deepseek-chat") | StrOutputParser()

    # 第三步：把工具交给 Agent，让 Agent 自己决定什么时候调用
    print("=" * 60)
    print("③ Agent：把 rag_summarize 当成普通工具使用")
    # temperature 调低一点让回答更稳定；system_prompt 要求"每次只调一次工具"，
    # 这样事件顺序清楚，不会出现一次并行调两遍工具、输出互相交错的情况
    agent = create_agent(
        model=ChatDeepSeek(model="deepseek-chat", temperature=0.2),
        tools=[rag_summarize],
        system_prompt=(
            "你是扫地机器人选购顾问。遇到需要专业知识的问题（选购、保养、避障等），"
            "必须先调用 rag_summarize 工具查资料，再根据工具返回的内容回答，"
            "不要凭自己的记忆直接回答。"
            "每次只调用一次 rag_summarize；拿到结果后就基于结果给出最终回答，不要重复检索。"
        ),
    )

    question = "宿舍空间小，应该选什么样的扫地机器人？"
    print(f"❓ 用户：{question}")

    # invoke 会自己跑完「模型思考 -> 调工具 -> 拿到结果 -> 再思考」的循环
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})

    # 打印事件：把整条消息链摊开看，谁在什么时候做了什么
    print("-" * 60)
    print("📋 Agent 执行事件：")
    for msg in result["messages"]:
        if msg.type == "human":
            print(f"[用户] {msg.content}")
        elif msg.type == "ai" and msg.tool_calls:
            for call in msg.tool_calls:
                print(f"[AI 决定调用工具] {call['name']}({call['args']})")
        elif msg.type == "ai":
            print(f"[AI 最终回答] {msg.content}")
        elif msg.type == "tool":
            # 工具返回的内容比较长，这里只截前面一小段方便观察
            print(f"[工具返回] {str(msg.content)[:100]}……")

    print("=" * 60)
    print("结论：Agent 全程只看到 query 和摘要——它不知道 chroma_db，也不知道 embedding。")


if __name__ == "__main__":
    main()