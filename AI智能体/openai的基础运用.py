import os
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
    ]
)
print(response.choices[0].message.content)
"""
这为ai的输出json格式
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "deepseek-flash",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "哼，谁、谁想你了！我只是刚好有空，才顺便回你一句而已……" // 你的print最终取出的就是这个
      },
      "finish_reason": "stop"
    }
  ],
  "usage": { ... }
}
"""