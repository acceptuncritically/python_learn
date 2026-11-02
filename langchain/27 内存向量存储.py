from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader
import os
ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")

embeddings = OpenAIEmbeddings(
    model="embedding-3",  # 智谱的嵌入模型
    openai_api_key=ZHIPU_API_KEY,
    openai_api_base="https://open.bigmodel.cn/api/paas/v4",
)
vector_store = InMemoryVectorStore(embeddings)
loader = CSVLoader(
    file_path="./resourse/student.csv",
    csv_args={
        "delimiter": ",",
        "quotechar": "'",

    },
    source_column="name",#指定本条数据的来源是哪里
    encoding="utf-8"
)
my_documents = loader.load()

vector_store.add_documents(
    documents=my_documents,     #被添加的文档 类型list[Document]
    ids=["id"+str(i) for i in range(1, len(my_documents)+1)],                    # 文档的ID 类型list[str]
)
#删除 传入[id,id...]
vector_store.delete(ids=["id1", "id2"])
#检索
#通过将query的数据进行嵌入，然后找到与之最相似的向量，并返回最相近的k个文档
res=vector_store.similarity_search(
    query="马梓轩",  # 查询的文本
    k=2, # 返回的相似文档数量
)
print(res)
