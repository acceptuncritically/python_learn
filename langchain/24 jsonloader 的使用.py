"""
{
    "name": "周杰伦",                    •  .表示整个JSON对象（根）
    "age": 11,                           •  []表示数组
                                          .[0]：表示提取数组的第1个元素（索引从0开始）。
    "hobby": ["唱", "跳", "RAP"],         •  .name表示抽取周杰伦
    "other": {                           •  .hobby表示抽取爱好数组
        "addr": "深圳",                  •  .hobby[1]或.hobby.[1]表示提取 hobby 数组的第2个元素（即 "跳"）
        "tel": "12332112321"             •  .other.addr表示抽取地址深圳
    }
}
[
    {"name": "周杰伦", "age": 11, "gender": "男"},    •  [].得到3个字典
    {"name": "蔡依林", "age": 12, "gender": "女"},    •  [].name 表示抽取全部的name，即得到3个name信息
    {"name": "王力宏", "age": 11, "gender": "男"}
]

"."：提取整个 JSON。
".user.info.name"：提取 user 对象下的 info 对象下的 name。
".[0]"：提取数组的第一个元素。
".[0].name"：提取数组第一个元素的 name。
".[] | .name"：管道符 |，先遍历数组 []，然后把遍历出的每个结果传给后面的 .name（效果等同于 .[].name）。
".users[] | select(.age > 10)"：高级用法，提取 users 数组中 age 大于 10 的元素。
"""
#对于单独数据的获取
from langchain_community.document_loaders import JSONLoader
loader = JSONLoader(
    file_path="./resourse/data.json",
    jq_schema=".other.addr",    #jq_schema 就像是一个“地址提取器”，你告诉 JSONLoader 怎么走
    text_content=False,     #告知JSONloader 抽取的内容不是字符串
)
document=loader.load()
print(document)
#获取JSON数组里的整个数据
loader = JSONLoader(
    file_path="./resourse/data1.json",
    jq_schema=".[].name",
    text_content=False,     #告知JSONloader 抽取的内容不是字符串
)

document=loader.load()
print(document)

loader = JSONLoader(
    file_path="./resourse/data2.json",
    jq_schema=".name",
    text_content=False,     #告知JSONloader 抽取的内容不是字符串
    json_lines=True         #告知JSONloader 这是一个JSONLINes文件 每一行都是一个标准的json
)
document=loader.load()
print(document)
