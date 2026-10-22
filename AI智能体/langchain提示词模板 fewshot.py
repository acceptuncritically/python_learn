# 1. 导入通用模板（永远来自 langchain_core）
from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate

# 2. 导入 DeepSeek 的模型适配器
from langchain_deepseek import ChatDeepSeek

example_template=PromptTemplate.from_template("单词：{word},反义词：{antonym}")

examples_data=[
    {"word":"大","antonym":"小"},
    {"word":"上","antonym":"下"}

]
#传入参数 构成为提示词模板
few_shot_templates=FewShotPromptTemplate(
    example_prompt=example_template,        #示例数据的模板
    examples=examples_data,              #示例的数据用来注入动态数据，list内套字典 必须是
    prefix="你是桑多涅，请根据我下面的示例"
           "将其对应的反义词输出",          #示例之前的提示词
    suffix="基于前面的示例傲娇的告诉我{input_word}的反义词是什么",                #示例之后的提示词
    input_variables=["input_word"]          #事先声明在前缀或后缀中的示例的名
)
prompt_text=few_shot_templates.invoke(input={"input_word":"左"}).to_string()
llm=ChatDeepSeek(model="deepseek-chat", temperature=0.7)

print(llm.invoke(input=prompt_text).content)