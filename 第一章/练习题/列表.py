# def count_sublists(list_input):
#     # 此处编写代码
from xml.etree.ElementInclude import default_loader


#     return sum(1 for i in list_input if type(i) == list)
# # 获取输入转为列表
# list_input = eval(input())
#
# # 调用函数
# print(count_sublists(list_input))

# -----------------------------------------------------------
# def find_largest_even(lst):
#
#
# # 此处编写你的代码
#     s=[i for i in lst if i%2==0]
#     return max(s,default=-1)    错误直接输出-1
#
# # 获取输入转为整数列表
# input_list = list(map(int, input().split()))
#
# # 调用函数
# print(find_largest_even(input_list))
# --------------------------------------------------------
# def is_consecutive_sequence(num_list):
#     # 此处编写你的代码
#     s=[]
#     i=0
#     num_list.sort()
#     while i<len(num_list):
#         if  num_list[i+1]-num_list[i]==1:
#             s.append(True)
#             if all(s):
#                 return True
#             else:
#                 return False
#
"""
all()如果结果全是true才会显示为True
any()如果有一个为False 则为False
"""
# # 获取输入转为整数列表
# nums = list(map(int, input().split()))
#
# # 调用函数
# print(is_consecutive_sequence(nums))
# ----------------------------------------------------------------
# def find_common_elements(list1, list2):
#     # 此处编写代码
#     s=[i for i in list2 if i in list1]
#     s.sort(reverse=False)
"""
reverse=True 
表示从大到小排列
reverse=False
表示从小到大排列
"""
#     return s
# # 获取用户输入，转换为列表
# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))
#
# # 调用函数
# print(find_common_elements(list1, list2))
# --------------------------------------------------------------------------
# def is_sum_present(num_list, target_sum):
# #     # 此处编写代码
# #
# #     for i in num_list:
# #         list1 = num_list.copy()
"""
在实际中如果将列表赋值为一个新列表
传递内存地址，会改变其列表中的内容
需要复制一个新列表
"""
# #         list1.remove(i)
# #         if target_sum-i in list1:
# #             return True
# #     return False
# # # 获取输入
# # num_list = list(map(int, input().split()))
# # target_sum = int(input())
# #
# # # 调用函数
# # print(is_sum_present(num_list, target_sum))
# -----------------------------------------------------------
# def count_frequency(lst):
# # 此处编写代码
#     dict1={}
#     set1={i for i in lst}
#     for j in set1:
#         dict1[j]=lst.count(j)
"""
常用将对应键值对添加进字典
"""
#     return set1
# # 获取用户输入
# lst = list(input().split())
#
# # 调用函数
# print(count_frequency(lst))
# -------------------------------------------------------------
# def can_form_target(list_of_lists, target_list):
# # 在这里编写你的代码
#     s=[]
#     for i in list_of_lists:
#         for j in i:
#             s.append(j)
#     s.sort()
#     if s==target_list:
#         return True
#     else:
#         return False
#
# # 获取用户输入
# user_list_of_lists = [list(map(int, input().split())) for _ in range(int(input()))]
"""
_表示不看重所取的元素，只看重循环的次数
整体意思就是 在循环输入次数下，将输入数字按照空格为区分，组成小列表，后再将小列表组成大列表
"""
# user_target_list = list(map(int, input().split()))
#
# # 调用函数
# print(can_form_target(user_list_of_lists, user_target_list))

# -----------------------------------------------------------
# def list_into_chunks(num_list, chunk_size):
#     chunks = []
#     for i in range(0, len(num_list), chunk_size):
#         chunks.append(num_list[i : i + chunk_size])
#     return chunks
"""
将列表通过具体的步长分成几部分
隔着去取分开片段的开始
num_list[i : i + chunk_size]
从索引 i 开始，连续截取 chunk_size 个元素

"""
# # 从用户输入中获取数据，并将其转换为列表
# num_list = list(map(int, input().split()))
# # 从用户输入中获取块大小
# chunk_size = int(input())
# # 调用函数
# print(list_into_chunks(num_list, chunk_size))
# ------------------------------------------------------------------------

# def missing_numbers_info(num_list):
#     # 此处写下你的代码
#     cnt = 0
#     sum_ = 0
#     for i in range(min(num_list), max(num_list)):
#         if i not in num_list:
#             cnt += 1
#             sum_ += i
#     yuan = cnt, sum_
#     return yuan
"""
列表转换为元组
yuan=(*cnt, *sum_)
输出: (1, 2, 3, 4, 5, 6)
yuan=(cnt,sum_)
输出: ([1, 2], [3, 4], [5, 6])
yuan=tuple(cnt+sum_)
输出: (1, 2, 3, 4)

数字转换为元组
yuan=(cnt,sum_)
yuan=cnt,sum_
"""
"""
基础转换：list()、tuple()、set() 闭眼套。
字符串转列表：优先用 .split()；列表转字符串用 ''.join()。
字典转换：转列表只拿键，要拿值加 .values()，要拿键值对加 .items()；
转字典必须用 zip() 或键值对列表。
组合技：sorted(list(set(my_list))) 是去重且排序的黄金公式。
"""
"""
列表用 []，如 [i for i in range(5)]，返回 list。
集合用 {}，如 {i for i in range(5)}，返回 set。
字典用 {} 且写 k:v，如 {i: i**2 for i in range(5)}，返回 dict。
生成器用 ()，如 (i for i in range(5))，返回 generator。
元组无推导式，需用 tuple() 转换，如 tuple(i for i in range(5))。
字符串无推导式，需用 ''.join() 拼接，如 ''.join(i for i in "abc")
"""
# 获取整数输入并将其转换为列表
# num_list = list(map(int, input().split()))
# # 调用函数
# print(missing_numbers_info(num_list))
# -----------------------------------------------------

# def get_all_permutations(digits):
#     # 在此处编写你的代码
#     for i in range(3):
#         for j in range(3):
#             for k in range(3):
#                 # 确保三个数字的索引不重复
#                 if i != j and j != k and i != k:
#                     # 将三个数字按顺序打印
#                     print(f"{digits[i]} {digits[j]} {digits[k]}")
"""
将三个数字重新组合输出
"""
# 获取整数输入并将其转换为列表
# digits = list(map(int, input().split()))
# # 调用函数
# get_all_permutations(digits)
# ----------------------------------------------------------

def break_down_list(items):
    # 此处编写代码
    s=[]
    for i in items:
        a=i["quantity"]
        for j in range(0,a):
            i["quantity"]=1
            s.append(i)
    return s
# 获取物品列表
items = eval(input())
# 调用函数，输出分解后的物品列表
print(break_down_list(items))