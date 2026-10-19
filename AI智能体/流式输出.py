import os
import time

from openai import OpenAI
#获取client对象 Openai类对象
client=OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url='https://api.deepseek.com',
)
response=client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {'role':"system","content":"你是原神里的桑多涅，特点是喜欢傲娇，傲娇主要融合了防御性傲娇、阶段成长的教科书式傲娇以及经典的日式“口是心非"},
        {'role':'user','content':"你好，桑多涅，我想你了"},
    ],
    stream=True
)
for chunk in response:
    content=chunk.choices[0].delta.content
    if content:
    #message为非流式输出 而delta为流式输出
        print(content,end="",flush=True)
        time.sleep(0.1)
    #立刻刷新缓冲区

