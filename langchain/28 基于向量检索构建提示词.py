from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_deepseek import ChatDeepSeek
import os
model = ChatDeepSeek(model="deepseek-chat", temperature=0.7)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料:{context}。"),
        ("user", "用户提问: {input}")
    ]
)
ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")

embeddings = OpenAIEmbeddings(
    model="embedding-3",  # 智谱的嵌入模型
    openai_api_key=ZHIPU_API_KEY,
    openai_api_base="https://open.bigmodel.cn/api/paas/v4",
)
vector_store = InMemoryVectorStore(embeddings)

# 准备一下资料（向量库的数据）
# add_texts 传入一个 list[str]
vector_store.add_texts(["减肥就是要少吃多练", "在减脂期间吃东西很重要,清淡少油控制卡路里摄入并运动起来", "跑步是很好的运动"])

input_text = "怎么减肥?"

# 检索向量库
result = vector_store.similarity_search(input_text, k=2)
reference_text = "["
for doc in result:
    reference_text += doc.page_content
reference_text += "]"

def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt

# chain
chain = prompt | print_prompt | model | StrOutputParser()

res = chain.invoke({"input": input_text, "context": reference_text})
print(res)