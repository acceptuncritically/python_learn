import os

# ✅ 修正 1：统一用“项目目录”的绝对路径。
# ❌ 原代码用 "./md5.text"、"./chroma" 这类相对路径，
#    从不同目录启动脚本（PyCharm / 终端 / streamlit）时会指向不同位置，
#    出现“明明上传过、rag.py 却查不到”的假象。
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

md5_path = os.path.join(BASE_DIR, "md5.text")
collection_name = "rag"
persist_directory = os.path.join(BASE_DIR, "chroma")
chunk_size = 1000
chunk_overlap = 10
separator = ["\n\n", "\n", " ", ""]
split_length = 500
session_config={"configurable": {"session_id": "test_session_id"}}

# ❌ 原代码：similarity_threshold = 1  # 返回检索数据的文档数量
#    名字叫“相似度阈值”，实际却在 vector_stores.py 里被当成 k 用（k=1）。
#    于是每次只把 1 个分块交给模型；faq.txt 被切成 3 块，问“公司上午几点上班”时
#    排名第 1 的是“加班/福利”段，真正含 9:00 的“考勤”段排第 2，模型自然答不出。
# ✅ 修正：改名为 top_k（它就是 k），取 4，保证同一资料的其他分块也能进入上下文。
top_k = 4

chat_model = "deepseek-chat"

# ---------------------------------------------------------------------------
# 智谱向量模型（Embedding）配置
# ⚠️ 知识库“入库”和“检索”必须使用【完全相同】的向量模型配置，
#    否则同一段文字在两边算出的向量不在同一个空间，检索结果会答非所问。
#    所以统一在这里创建，knowledge_base.py(入库) 和 rag.py(检索) 都调用它。
# ---------------------------------------------------------------------------
embedding_model = "embedding-3"  # 智谱向量模型，默认输出 2048 维
embedding_base_url = "https://open.bigmodel.cn/api/paas/v4"


def get_embeddings():
    """创建智谱向量模型客户端（入库、检索共用，保证两边配置完全一致）。"""
    # 延迟导入：只有真正用到向量库时才 import 这个包
    from langchain_openai import OpenAIEmbeddings

    api_key = os.getenv("ZHIPU_API_KEY")
    if not api_key:
        raise RuntimeError(
            "环境变量 ZHIPU_API_KEY 未设置。请先配置智谱 API Key，例如：\n"
            '    setx ZHIPU_API_KEY "你的key"   # 然后重开终端 / 重启 PyCharm'
        )
    return OpenAIEmbeddings(
        model=embedding_model,
        openai_api_key=api_key,
        openai_api_base=embedding_base_url,
        # ⚠️ 关键：智谱的 OpenAI 兼容接口只接受纯文本，不接受 OpenAI 那种
        #    “token id 数组”。langchain_openai 默认会先用 tiktoken 分词、再把
        #    token id 数组发给接口(check_embedding_ctx_length=True)：接口不报错，
        #    但返回的是“token 串”的向量，和正常文本向量完全不在一个空间
        #    → 检索结果全乱。对接第三方 OpenAI 兼容接口时必须关闭它。
        check_embedding_ctx_length=False,
    )
