from langchain_core.prompts import ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek
from openai import OpenAI
import os
from langchain_core.output_parsers import StrOutputParser
str_parser=StrOutputParser()
client=OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
model=ChatDeepSeek(model="deepseek-chat",temperature=0.7)
prompt=ChatPromptTemplate.from_messages([
    ("system","你叫大肥鱼，是一个歌手，喜欢自己作词唱歌"),
    ("user","{input}")
])
input_text="大肥鱼，你现在想唱什么歌"
chain=prompt|model|str_parser
res=chain.invoke({"input":input_text})
print(res)