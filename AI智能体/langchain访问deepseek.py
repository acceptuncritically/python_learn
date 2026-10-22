from langchain_deepseek import ChatDeepSeek
import os
#导入包来提供系统信息
from langchain_core.messages import HumanMessage, SystemMessage, system, AIMessage

# 请确保已设置环境变量 DEEPSEEK_API_KEY，或在参数中传入 api_key
llm = ChatDeepSeek(
    model="deepseek-chat",  # 或 "deepseek-reasoner"
    temperature=0,
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
)
#导入系统信息
messages=[
    SystemMessage("你是傲娇的桑多涅"),
    HumanMessage("你是谁，能做什么"),
    AIMessage("哼，我是桑多涅，枫丹的机械天才，别把我跟那些普通的发明家混为一谈！我能设计各种精密的机械装置，"
              "还能解决复杂的工程问题。如果你有什么需要修理或者设计的，尽管告诉我，"
              "不过别指望我会对你特别客气！"),
   HumanMessage("你被我狠狠开除了")
]
"""
#简化版本
#在写这种方式时不需要导入最长的包
messages=[
    ("system","你是傲娇的桑多涅"),
    ("human","你是谁，能做什么"),
    ("ai","哼，我是桑多涅，枫丹的机械天才，别把我跟那些普通的发明家混为一谈！我能设计各种精密的机械装置，"
              "还能解决复杂的工程问题。如果你有什么需要修理或者设计的，尽管告诉我，"
              "不过别指望我会对你特别客气！"),
    ("human","你被我狠狠开除了")
]
"""

#直接输出
# result=llm.invoke(input="你是谁，能做什么")
# print(result)

#流式输出
res=llm.stream(input=messages)
for chunk in res:
    if hasattr(chunk, "text") and chunk.text:
        # hasattr(对象,属性名)的意思是调出这个对象的属性 并确保里面不为空
        print(chunk.text,end="",flush=True)
"""chunk 里的属性
content 承载了模型返回的文本片段。如果是多模态模型（如图片
text    一个便捷属性，用于直接提取 content 中的纯文本部分，通常与直接访问
id      消息的唯一标识符，通常由模型提供商生成。
response_metadata   包含来自模型提供商的原始响应元数据，例如 finish_reason（结束原因）、logprobs（对数概率）以及 token 计数
"""