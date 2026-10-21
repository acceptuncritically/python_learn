"""
json.dumps(字典或列表, ensure_ascii=False): 将字典或列表转换为Json字符串
ensure_ascii参数确保中文能正常显示
返回值：Json字符串

json.loads(json字符串): 将Json字符串转换为Python字典或列表
返回值：Python字典 或 Python列表
json里要用双引号
"""
import json
d={
    "name":"桑多涅",
    "age":18,
    "gender":"女",
}
s=json.dumps(d, ensure_ascii=False)
print(s)
list1=[
    {
        "name": "哥伦比亚",
        "age": 18,
        "gender": "女",
    },
    {
        "name": "仆人",
        "age": 18,
        "gender": "女",
    }
]
result=json.dumps(list1, ensure_ascii=False)
print(result)
json_str='{"name":"桑多涅","age":18,"gender":"女"}'
json_str2='[{"name": "哥伦比亚","age": 18,"gender": "女"},{"name": "仆人","age": 18,"gender": "女"}]'
json_str_result=json.loads(json_str)
json_str2_result=json.loads(json_str2)
print(json_str2_result)
print(json_str)