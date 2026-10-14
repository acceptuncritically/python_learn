def get_unique_elements(nested_tuples):
    # 此处编写代码
    s1 = set()

    # 遍历嵌套元组中的每一个子元组
    for tup in nested_tuples:
    # 使用 update() 方法将子元组中的元素添加到集合中（自动去重）
        s1.update(tup)
    # 使用 sorted() 将集合排序，它会自动返回一个列表
    return sorted(s1)
# 初始化嵌套元组
nested_tuples = []
"""
set.update(可遍历元素) —— 集合的“批量添加”方法
会自动去重，会直接修改原来的集合
dirt也有update 会直接添加
sorted() —— 万能排序函数
任何类型都能排序
返回一个列表
"""
# 获取用户输入
for _ in range(3):
    tuple_elements = tuple(map(int, input().split()))
    nested_tuples.append(tuple_elements)

# 调用函数
print(get_unique_elements(nested_tuples))