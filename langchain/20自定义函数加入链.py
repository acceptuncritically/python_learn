from langchain_core.output_parsers import StrOutputParser
from langchain_deepseek import ChatDeepSeek
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate

#创建所需的解析器
str_parser=StrOutputParser()
my_function=RunnableLambda(lambda x: {"name": x.content})
#创建一个模型
model=ChatDeepSeek(model="deepseek-chat", temperature=0.7)
#第一个提示词模板
first_prompt = PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了{gender},你取个名字"
    "仅仅告诉我名字"
)
#第二个提示词模板
second_prompt = PromptTemplate.from_template(
    "姓名：{name}，请帮我解析其含义"
)
#创建一个链
#可以直接把函数写在其中 因为在调用时 会直接转化为RunnableLambda对象
chain=first_prompt|model|my_function|second_prompt|model|str_parser
for chunk in chain.stream({"lastname":"芦","gender":"女儿"}):
    print(chunk,end="",flush=True)