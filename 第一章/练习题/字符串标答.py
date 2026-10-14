def is_date_palindromic(date_in_string):
    # 1. 拆分输入字符串，获取 日(dd), 月(mm), 年(yyyy)
    parts = date_in_string.split("/")
    dd = parts[0]
    mm = parts[1]
    yyyy = parts[2]

    # 2. 检查 dd/mm/yyyy 格式
    # 拼成 ddmmyyyy 并去掉斜杠
    date_ddmm = dd + mm + yyyy
    # 判断是否回文（正序等于逆序）
    is_ddmm_palindrome = (date_ddmm == date_ddmm[::-1])

    # 3. 检查 mm/dd/yyyy 格式
    # 拼成 mmddyyyy 并去掉斜杠
    date_mmdd = mm + dd + yyyy
    is_mmdd_palindrome = (date_mmdd == date_mmdd[::-1])

    # 4. 两个格式都必须满足回文，才返回 True
    return is_ddmm_palindrome and is_mmdd_palindrome


# 获取输入
sentence = input()

# 调用函数并打印
print(is_date_palindromic(sentence))
"""
编写一个程序，检查给定日期是否为dd/mm/yyyy和mm/dd/yyyy格式的回文日期。
定义函数is_date_palindromic()，接受一个参数date_in_string（以dd/mm/yyyy格式的日期字符串）。
如果给定的日期在dd/mm/yyyy和mm/dd/yyyy格式下都是回文日期，函数应该返回True，否则返回False。
"""
------------------------------------------------