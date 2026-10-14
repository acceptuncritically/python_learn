# def calculate_days_between(date1, date2):
#     # 在此处编写你的代码
#     s1=date1.split("-")
#     s2=date2.split("-")
#     print(s1)
#     cha=(int(s2[1])-int(s1[1]))*30+int(s2[2])-int(s1[2])
#     return cha
#
# # 获取用户输入
# date1 = input()
# date2 = input()
#
# # 调用函数
# print(calculate_days_between(date1, date2))
# -----------------------------------------------
# def shift_char(word):
#     # 此处编写你的代码
#     s=[]
#     for i in word:
#         i=chr(ord(i)+1)
#         s.append(i)
#     return ''.join(s)
# # 获取单词
# word = input()
# # 调用函数
# print(shift_char(word))
# ------------------------------------------
# def get_missing_letters(word_string):
#     # 此处编写你的代码
#     s=[j for j in range(97,123)]
#     for i in word_string:
#         s.remove(ord(i))
#     return ''.join([chr(k) for k in s])
"""
将列表最终变为一个字符串
"""
# # 获取输入的字符串
# word_string = input()
#
# # 调用函数输出结果
# print(get_missing_letters(word_string))
# -------------------------------------------------
# def count_duplicate_chars(input_string):
#     # 在此处编写你的代码
#     a=[]
#     s=list(input_string)
#     for i in set(input_string):
#         if s.count(i)>1:
#             a.append(s.count(i))
#     return len(a)
# # 获取用户输入
# test_string = input()
#
# # 调用函数
# result = count_duplicate_chars(test_string)
# print(result)
# --------------------------------------------------------
# def count_char_occurrences(sentence, char):
#     # 此处编写你的代码
#     k=[]
#     a=sentence.lower()
#     s=a.split(" ")
#     for i in s:
#         cnt=0
#         for j in range(0,len(i)):
#             if char==i[j]:
#                 cnt+=1
#         k.append(cnt)
#     return k
# # 获取输入
# sentence_input = input()
# char_input = input()
# # 调用函数
# print(count_char_occurrences(sentence_input, char_input))
"""
# 题目要求将句子转为小写，为了忽略大小写，char也转小写
char = char.lower()
# sentence.lower() 转小写，split() 默认按空白字符（空格、换行等）分割成单词列表
words = sentence.lower().split()
# 使用列表推导式，遍历每个单词，用 count() 统计 char 出现的次数
return [word.count(char) for word in words]
"""
# -------------------------------------------------------
# def add_space_before_capital(word):
#     result = ""
#     for char in word:
#         if char.isupper():
#             result += " " + char
#         else:
#             result += char
#     return result.lower()
# """
# 字符串可以直接相加
# """
# # 测试
# print(add_space_before_capital("myNewComputer"))  # 输出: my new computer
# ---------------------------------------------------
# def get_longest_word(sentence):
#     # 在此处编写你的代码
#     a = sentence.split()
#     return max(a, key=len)
"""
key=len
原本max是找寻最大值，就是直接比较元素本身，并返回那个“最大”的元素。
它返回的是原对象
加上就是以长度最大值进行比较并输出最大值所对应的对象
"""
# # 获取输入
# sentence = input()
#
# # 调用函数
# print(get_longest_word(sentence))
# ----------------------------------------------------
# def is_sum_even(string):
#     # 此处编写你的代码
#
#     total=0
#     string1 = string.lower().split()
#     for i in string1:
#         for j in range(0,len(i)):
#            total+=(ord(i[j])-96)
#     if total%2==0:
#         return True
#     else:
#         return False
#
#
#
# # 获取字符串
# string = input()
#
# # 调用函数
# print(is_sum_even(string))
# --------------------------------------
# def reverse_binary_integer(n):
#     # 此处编写你的代码
#     a = format(n, 'b')
#     s = a[::-1]
#     return int(s, 2)
a="""
format 输入可以是任何容器 输出都是字符串
但当要转换进制时要是整数 b 二进制 d十进制 f是浮点数
[::-1]可以省略开头和结尾 -1表示从后往前一个一个取
int（字符串，进制数） 进制数表示当前字符串的数字的进制，输出将会转换为十进制
如果没有进制数，浮点数将会转换为整数
"""
# 获取输入
# n = int(input())
#
# # 调用函数
# print(reverse_binary_integer(n))
# -------------------------------------------------
# def capitalize_last_letter(sentence):
#     # 此处编写你的代码
#     s=sentence.split()
#     result=""
#     for i in s:
#         a=i[:-1]+i[-1].upper()
#         result=result+a+" "
#     return result
#
# # 获取输入
# sentence = input()
#
# # 调用函数
# print(capitalize_last_letter(sentence))
# --------------------------------------------
# def is_date_palindromic(date_in_string):
#     a=date_in_string.split('/')
#     list1=list(''.join(a))
#     result1=list1.copy()
#     list1.reverse()
#     if result1==list1:
#             a[0],a[1]=a[1],a[0]
#             list2 = list(''.join(a))
#             result2=list2.copy()
#             list2.reverse()
#             if result2==list2:
#                 return True
#     return False
# # 此处编写你的代码
# # 获取日期输入
# date_in_string = input()
#
# # 调用函数
# print(is_date_palindromic(date_in_string))
# -----------------------------------------
# def common_letters(word1, word2):
#     # 此处编写代码
#     #先找到两者共有的字母
#     s1=set(word1)
#     s2=set(word2)
#     gong= ''.join(sorted(list(s1.intersection(s2))))
#     # 如果有
#     if gong =='':
#         return ''
#     else:
#        return gong
#
# # 输入两个单词
# word1 = input()
# word2 = input()
#
# # 调用函数, 并打印结果
# print(common_letters(word1, word2))
# -----------------------------------------
# def is_string_palindrome(string):
#     # 此处编写代码
#
#     if string[::-1]==string:
#         return True
#     else:
#         return False
# # 获取用户输入
# user_input = input()
#
# # 调用函数
# print(is_string_palindrome(user_input.lower()))
# -----------------------------------------------
# def sort_by_last_char(sentence):
#     # 此处编写代码
#     s = sentence.split(" ")
#     s.sort(key=lambda x: x[-1])
#     return ' '.join(s)
"""对列表 s 原地排序，排序时不是直接比较元素本身，
而是先对每个元素 x 调用 lambda x: x[-1]，用它的返回值作为排序依据
"""
# 输入句子
# sentence = input()
#
# # 调用函数
# print(sort_by_last_char(sentence))
# ----------------------------------------
# def sort_words_by_char(words, index):
#     # 在此处编写代码
#     words.sort(key=lambda x: x[index - 1])
#     return words
# 获取用户输入
# words = input().split() # 单词列表
"""这行代码的作用是：从键盘读取一行输入，
按空白字符分割成多个部分，存成 字符串列表，赋值给 words
"""
# index = int(input())    # 位置
#
# # 调用函数
# print(sort_words_by_char(words, index))
# -------------------------------------
# def convert_str_list_to_dict(str_list):
#     # 此处编写代码
#     str_list1=str_list.split(" ")
#     result = {}
#     for item in str_list1:
#         key, value = item.split('=')
#         result[key] = value
#     return result
# # 输入字符串
# str_list = input()
#
# # 调用函数
# print(convert_str_list_to_dict(str_list))
# ------------------------------------------------
# def repetitions_in_string(s):
#     # 此处编写代码
#     list1=[]
#     for i in range(1,len(s)+1):
#         d=s[0:i:1]
#         list1.append(d)
#
# # 获取输入
# test_string = input()
#
# # 调用函数
# print(repetitions_in_string(test_string))
# ---------------------------------------
# def repetitions_in_string(s):
#     n = len(s)
#     for length in range(1, n // 2 + 1):
#         if n % length == 0:
#             sub = s[:length]
#             if sub * (n // length) == s:
#                 return n // length
#     return 1
# # 获取输入
# test_string = input()
#
# # 调用函数
# print(repetitions_in_string(test_string))
# -----------------------------------------------
def is_heterogram(s):
    # 此处编写代码
    s1=s.split(" ")
    list1=list(''.join(s1))
    for i in list1:
        if list1.count(i)>1:
            return "No"
    else:
        return "Yes"
# 获取输入
input_string = input()

# 调用函数，输出结果
print(is_heterogram(input_string))