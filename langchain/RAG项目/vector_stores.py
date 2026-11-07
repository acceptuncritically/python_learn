from langchain_chroma import Chroma
import config_data as config


class VectorStores:
    def __init__(self, embedding):
        self.embedding = embedding
        self.vector_stores = Chroma(
            persist_directory=config.persist_directory,
            embedding_function=self.embedding,
            collection_name=config.collection_name
        )

    def get_retriever(self):
        """返回向量检索器方便加入chain"""
        # ❌ 原代码：search_kwargs={"k": config.similarity_threshold}
        #    similarity_threshold 名字是“相似度阈值”，却被当成“返回文档数量 k”，
        #    且值只有 1 → 只取 1 个分块，检索到不含答案的分块时模型就答不出。
        # ✅ 修正：数量用 config.top_k，语义清晰。
        return self.vector_stores.as_retriever(search_kwargs={"k": config.top_k})


if __name__ == "__main__":
    # 与 knowledge_base.py 入库时使用完全相同的向量模型配置
    retriever = VectorStores(config.get_embeddings()).get_retriever()
    res = retriever.invoke("公司几点上班")
    print(res)
