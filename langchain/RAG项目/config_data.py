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

# ❌ 原代码：similarity_threshold = 1  # 返回检索数据的文档数量
#    名字叫“相似度阈值”，实际却在 vector_stores.py 里被当成 k 用（k=1）。
#    于是每次只把 1 个分块交给模型；faq.txt 被切成 3 块，问“公司上午几点上班”时
#    排名第 1 的是“加班/福利”段，真正含 9:00 的“考勤”段排第 2，模型自然答不出。
# ✅ 修正：改名为 top_k（它就是 k），取 4，保证同一资料的其他分块也能进入上下文。
top_k = 4

chat_model = "deepseek-chat"
