def swap_dict(dict):
    s={}
    for key, value in dict.items():
        if value not in s:
            s[value] = [key]
        else:
            s[value].append(key)
    return s

# 此处编写代码

# 读取输入的字典
dict = eval(input())

# 调用函数
print(swap_dict(dict))
# -----------------------------------
def count_common_vowel(string):
    list1=string.split(" ")
    dict={}
    a=[]
    for i in list1:
        a.append(i[-1])
        for j in a:
            if j in "aeiou":
                a.count(j)
                dict[j]=a.count(j)
    yuanyin=max(dict,key=dict.get)
    """
    先输入对比的容器 key后跟着想要按什么规则进行比较
    """
    return yuanyin
string = input()
result = count_common_vowel(string)
print(result)
# ----------------------------------------