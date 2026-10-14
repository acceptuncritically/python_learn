from unittest import case

# day=input("输入今天星期几：")
# match day:
#     case "1":
# #不能空着
#         print("")
#     case "2":
#         print("星期二")
#     case "3"|"4":
#         print("都可以")
#     case _:
#         print("其他情况")

# 实行加减乘除，用户通过输入数字 来选择加减乘除
a=float(input("输入数字："))
b=float(input("输入数字："))
num=int(input("输入数字确定运算方式："))
match num:
    case 1:
        print(f"{a}+{b}={a+b}")
    case 2:
        print(f"{a}-{b}={a-b}")
    case 3:
        print(f"{a}*{b}={a*b}")
    case 4 if b != 0 :
        #match 支持这种条件判断
         print(f"{a}/{b}={a/b}")
    case _:
        print("输出错误")