# 通过字词语 找到对应该词的解释
# 每个字词一一对应
# 字词不能重复
# 里面存储键值对类型的数据可以根据键找到对应的值（key：value）


# 定义列表存储
name_list = ["王林", "韩立", "李慕婉", "紫灵", "许立国", "王政", "张紫"]
score_list = [670, 556, 582, 435, 608, 512, 678]

# 定义字典存储
dict1 = {"王林": 670, "韩立": 556, "李慕婉": 582, "紫灵": 435, "许立国": 608, "王政": 512, "张紫": 678}
#key保证不重复 里面的内容可修改
# 定义一个空字典
dict2={}
dict3=dict()
score=dict1["许立国"]
print(score)
#value里可以是可变类型如列表 字符串  key里是不可变类型
"""
列表 (list)：例如 [1, 2] 会报错。

字典 (dict)：例如 {"a": 1} 会报错。

集合 (set)：例如 {1, 2} 会报错。

包含可变元素的元组
"""
dict_={0:670,1.5:608,(1,2):580,"a":200}
print(dict_["a"])
"""
添加    往指定字典中添加key-value键值对   dict1["tao"]=688
删除   删除字典中指定的key，并返回该key对应的value   score=dict1.pop("tao")
      删除字典中指定的键值对                 del dict1["tao"]
修改    修改字典中指定的key对应的 值         dict1["tao"]=688
查询        根据key获取value                   dict1["tao"]
        根据key获取value                   dict1.get["tao"]
        获取所有的key                     dict1.keys()
        获取所有的value                     dict1.value()
          获取所有的key-value键值对            dict1.items()
"""

dict1 = {"王林":670, "李慕婉":608, "许立国":580, "韩立":688}
print(dict1)

# 添加 - key不存在就是添加
dict1["涛哥"] = 550
print(dict1)

# 修改 - key存在就是修改
dict1["涛哥"] = 620
print(dict1)

# 查询
print(dict1["涛哥"])  # 根据key获取value
print(dict1.get("涛哥"))  # 根据key获取value

print(dict1.keys())  # 获取所有的key   会封装到dict.keys
print(dict1.values())  # 获取所有的value
print(dict1.items())  # 获取所有的键值对 key:value

# 删除
score = dict1.pop("许立国")
print(score)
print(dict1)

del dict1["韩立"]
print(dict1)

#遍历
for k in dict1.keys():
    print(f"{k}: {dict1[k]}")
for v in dict1.items():
    print(f"{v[0]}: {v[1]}")