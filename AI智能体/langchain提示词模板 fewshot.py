"""
  1  导入langchain里的 FewShotPromptTemplate 用来定义一个管理类 用它去管理每一个小的个体
                    PromptTemplate 用来定义一个个体类
    导入deepseek 要接入的大语言模型的包
  2  PromptTemplate 用来定义一个小模版，
     FewShotPromptTemplate 用来定义大模板装有多个小模版
        1.example_prompt 装里面的PromptTemplate定义的小模版
        2.examples 用列表套字典的方式 达到多个小模版的效果
        3.prefix 在示例模板之前的提示词
        4.suffix 在示例之后的提示词 在提示词中用变量名来输入想问的具体示例
        5.input_variables 在suffix里的变量名，用列表的方式存储
  3. 提示词模板调用invoke方法(input={"input_word":"左"}).to_string() 用字典形式传入input_variables的值
  4.调用大语言模型 ChatDeepSeek(model="deepseek-chat", temperature=0.7) temperature表示大语言模型的保守程度
  5. 大语言模型调用invoke(input=将3的结果传入进来).content 输出模型回答的内容
"""
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