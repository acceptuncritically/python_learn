# def calculate_sum(numbers_list):
#     # 此处编写代码
#     even_sum=0
#     odd_sum=0
#     for i in numbers_list:
#         if numbers_list[i]%2==0:
#                 even_sum+=numbers_list[i]
#         else: odd_sum+=numbers_list[i]
#     return even_sum,odd_sum
# # 获取输入转为列表
# numbers_list = list(map(int,input().split()))
#
# # 打印偶数和奇数的和
# print(calculate_sum(numbers_list))

# def add_numbers(num1, num2):
#     # 此处编写代码
#     if num1 in (None, "") or num2 in (None, ""):
#         return "Invalid Operation"
#     else:
#         return str(int(num1)+int(num2))
# # 获取用户输入num1 和 num2
# num1 = input()
# num2 = input()
#
# # 调用函数
# result = add_numbers(num1, num2)
#
# # 打印和
# print(result)

# def is_harshad(num):
#     # 在此处编写你的代码
#     cnt=0
#     s=str(num)
#     list1=list(s)
#     for i in list1:
#         cnt+=int(i)
#     if num%cnt==0:
#         return True
#     else:
#         return False
# # 获取用户输入
# num = int(input())
#
# # 显示输出
# print(is_harshad(num))

# def is_title(sentence):
#     # 在此处编写代码
#     s=sentence.split(' ')
#     for i in s:
#         if not i[0].isupper():
#             return False
#     return True
# # 从用户处获取输入
# input_sentence = input()
# # 调用函数
# print(is_title(input_sentence))

# def find_unique(lst):
#     # 此处编写代码
#     s=[]
#     for i in lst:
#         if lst.count(i) == 1:
#             s.append(i)
#     return s
# # 获取用户输入并转为数字列表
# numbers = list(map(int, input().split()))
#
# # 调用函数
# print(find_unique(numbers))


# def check_double_base_palindrome(number):
#     """
#     编写一个程序来检查一个数字是否是双基回文数。
#
# 回文是指从前往后读和从后往前读都一样的字母、数字的序列。
#
# 双基回文数是指在十进制和二进制表示中都是回文的数字。
#     :param number:
#     :return:
#     """
#     # 此处编写代码
#     s=[int(i) for i in str(number)]
#     s1 = s.copy()
#     s.reverse()
#     er=[i for i in format(number,"0b")]
#     er1 = er.copy()
#     er.reverse()
#     if s1==s and er==er1:
#         return True
#     else:
#         return False
# # 获取用户输入
# number = int(input())
#
# # 调用函数
# print(check_double_base_palindrome(number))


# def find_indices(my_list, element):
# #     # 此处编写代码
# #     """
# #     编写一个程序，查找给定列表中给定元素的所有索引。
# #
# # 定义函数find_indices()，它接受两个参数，一个my_list列表和一个element的变量。
# # 该函数应返回my_list中出现element的所有索引的列表。
# #     :param my_list:
# #     :param element:
# #     :return:
# #     """
# #     s=[]
# #     index_=-1
# #     for i in user_input:
# #         index_+=1
# #         if element == i:
# #             s.append(index_)
# #     return s
# # # split()函数将输入的字符串分割成一个列表
# # user_input = input().split()
# # element = input()
# #
# # # 调用函数
# # print(find_indices(user_input, element))


# def shared_chars_count(word1, word2):
#     # 此处编写代码
#     """
#     cnt=0
#     lista = list(word1)
#     lista1=[]
#     for i in lista:
#         if i not in lista1:
#             lista1.append(i)
#     listb = list(word2)
#     listb1=[]
#     for j in listb:
#         if j not in listb1:
#             listb1.append(j)
#     for i in lista1:
#         for j in listb1:
#             if i == j:
#                 cnt+=1
#     return cnt
#     """
#     return len(set(word1) & set(word2))
# # 获取输入
# word1 = input()
# word2 = input()
#
# # 调用函数
# print(shared_chars_count(word1, word2))

# def sum_missing_numbers(nums):
#     _sum=0
#     for i in range(min(nums)+1,max(nums)):
#         if i not in nums:
#             _sum+=i
#     return _sum
#
# # 此处编写代码
#
# # 获取输入转为数字列表
# nums = list(map(int, input().split()))
#
# # 调用函数
# print(sum_missing_numbers(nums))



# def dict_to_sorted_list(dictionary):
#     # 此处编写你的代码
#     s=[]
#     for k in dictionary.keys():
#         a=[k,dictionary[k]]
#         s.append(a)
#         s.sort(reverse=False)
#     return s
# # 获取输入转为字典
# dictionary = eval(input())
#
# # 调用函数
# print(dict_to_sorted_list(dictionary))

def count_consonants(word):
    # 在此处编写你的代码
    yuanyin = ["a", "e", "i", "o", "u"]
    return sum(1 for i in word if i not in yuanyin)


def count_vowels(word):
    # 在此处编写你的代码
    yuanyin = ["a", "e", "i", "o", "u"]
    return sum(1 for i in word if i in yuanyin)
# 如何“忽略数字、特殊字符和空格”？
# 使用字符串内置方法 char.isalpha()。如果字符是英文字母（a-z, A-Z），
# 它返回 True；如果是数字、空格、标点符号，它返回 False。这样就能自动过滤掉不需要的字符

# 获取用户输入
word = input()

# 调用函数
print(count_consonants(word))
print(count_vowels(word))