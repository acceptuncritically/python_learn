"""
chain=prompt|model|model 链式法则没有错
但prompt的结果是promptvalue类型输入给了model
model的输出结果是AImessage
在调用invoke方法时会报错 由于invoke方法里要求input 是promptvalue str 或者Sequence
可以借助LangChain内置的解析器 StrOutputParser字符串输出解析器 可以将AIMessage转换为str
是Runnable接口的子类 可以加入链
"""
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_deepseek import ChatDeepSeek

#创建一个解析器
parser=StrOutputParser()
model=ChatDeepSeek(model="deepseek-chat", temperature=0.7)
prompt=PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了{gender},请你直接输出你要起的名字"
)
chain=prompt|model|parser|model
res:AIMessage=chain.invoke({"lastname":"芦", "gender":"女儿"})
print(res.content)
