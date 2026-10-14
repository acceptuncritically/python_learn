#   if 条件：
#       随从语句

#根据用户输入内容 来判断是闰年 还是平年
#正百时要除以400能够整除才算为闰年

num=int(input("你要判断的年份："))
if (num%100!=0 and num%4 == 0) or num%400==0:
    print(f"{num}是闰年")
else:print(f"{num}是平年")

#f"{num}" 可以“格式化”任何类型为字符串，
# 但不能“替代”任何类型。它输出的是 str，不是原对象。

# if elif else 满足第一个条件就不会判断第二部分 1 2都不满足进入else

#案例：根据输入的用户名和密码进行登录  admin/666888  root/54321  zhangsan/123456
username=input("输入用户名:")
password=input("输入密码:")

if username=="admin" and password=="666888":
    print("登陆成功")
elif username=="root" and password=="54321":
    print("登陆成功")
elif username=="zhangsan" and password=="123456":
    print("登陆成功")
else:print("登陆失败")


#三角形类型判断  判断是等腰等边 普通 还是不能够构成

print("依次输入三角形的三条边：从大到小\n")
a=int(input(""))
b=int(input(""))
c=int(input(""))

if a+b>c and a+c>b and b+c>a:  #可以构成三角形
    if a==b and b==c:
        print("构成等边三角形")
    elif a==b or b==c or a==c:
        print("构成等腰三角形")
    else:
        print("构成普通三角形")
else:
    print("不能构成三角形")