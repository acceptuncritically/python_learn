def dict_to_sorted_list(dictionary):
    # 此处编写你的代码
    """
    将字典转换成列表
    :param dictionary:
    :return:
    """
    s=[]
    for k in dictionary.keys():
        a=[k,dictionary[k]]
        s.append(a)
        s.sort(reverse=False)
    return s
# 获取输入转为字典
dictionary = eval(input())

# 调用函数
print(dict_to_sorted_list(dictionary))