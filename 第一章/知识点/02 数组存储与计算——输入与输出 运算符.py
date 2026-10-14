# input函数 s=input(输入内容)
#
# 无论输入的是什么类型，最终获得到的永远是字符串

#银行取钱
total=1000
cost=input ("你要取多少钱：")

# sheng=total -int(cost)    int(将字符串转换为整型)
# print (f"{sheng}")

print(f"{total -int(cost)}")

#运算符 算术 赋值 比较 逻辑
#算数 + - * /(除法)  //(整除)  %   **（幂运算）
# 优先级 ** * / // % + -

x=float(input(""))
y=float(input(""))
print(x+y)
print(x-y)

# 0.09999999999998    精度损失 二进制无法准确表示所有的小数，涉及浮点数运算时，会损失

#赋值运算符：与c相同 += *= /=  //=  **=
#比较运算符  计算表达式并输出一个布尔值 True 或 False
#逻辑运算符  返回一个布尔值 and 与  or 或  not  非 True变False
n=int(input("输入一个整数"))
# print(f"是否在10 20 间", 10 <= n <= 20)
print(f"是否在10 20 间", n>=10 and n<=20)