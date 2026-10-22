
"""将字符串作为输入，返回一个浮点数的列表
由于deepseekAPI不提供将数据转化为向量的模型，所以用GLM
"""
from langchain_openai import OpenAIEmbeddings
import os

# 1. 替换为你从智谱AI平台获取的 API Key
ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")

# 2. 初始化智谱的嵌入模型
embeddings = OpenAIEmbeddings(
    model="embedding-3",  # 智谱的嵌入模型
    openai_api_key=ZHIPU_API_KEY,
    # 注意：智谱的 base_url 与 DeepSeek 不同
    openai_api_base="https://open.bigmodel.cn/api/paas/v4",
)

# 3. 测试调用
try:
    query_vector = embeddings.embed_query("我喜欢你")
    print(query_vector) #2048维向量
    print(f"向量维度: {len(query_vector)}")  # 智谱 embedding-3 的维度为 2048

    #把数据转换为向量在存储到向量库中
    doc_vectors = embeddings.embed_documents(['我喜欢你', '我稀饭你', '晚上吃啥'])
    print(f"文档数量: {len(doc_vectors)}")

except Exception as e:
    print(f"调用失败: {e}")