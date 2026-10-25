"""
    1  导入langchain里的PromptTemplate 用来定义一个个体类
       导入deepseek 要接入的大语言模型的包
    2. 调用大语言模型
    3.  PromptTemplate 用from_template方法定义一个小模版，里面含有占位词，用来传入想改变的提示词
    4.  将提示词模板 用format方法 传入提示词模板中的占位词
    5.  大语言模型使用invoke方法将模板传进来 并输出返回的结果
"""
# 1. 导入通用模板（永远来自 langchain_core）
from langchain_core.prompts import PromptTemplate

# 2. 导入 DeepSeek 的模型适配器
from langchain_deepseek import ChatDeepSeek

# 3. 初始化 DeepSeek 模型
llm = ChatDeepSeek(model="deepseek-chat", temperature=0.7)

# 4. 创建提示词模板
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了{gender},请你直接输出你要起的名字"
)
#用其中的format方法将占位符换为其中的内容
prompt_text=prompt_template.format(lastname="芦", gender="女儿")

# 6. 传入变量，执行链
response = llm.invoke(prompt_text)
print(response.content)