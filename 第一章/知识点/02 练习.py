    # 现有三个变量，分别为a=100，b=200，c=300，将a b c的值交换给cab
# a=100
# b=200
# c=300
# d=c
# c=a
# a=b
# b=d
# print(a,b,c)

    #根据直角边的边长，打印直角三角形

# cnt=int(input("边长为："))
# for i in range(1,cnt+1):
#     for j in range(1,i+1):
#         print("*",end="\t")
#     print()

    #根据输入的数字，打印对应的数字金字塔

# cnt=int(input("输入数字："))
# for i in range(1,cnt+1):
#     for j in range(1,i+1):
#
#             print(j,end="\t")
#     print()

    #打印国际象棋棋盘

# for i in range(1,6):
#     for j in range(1,6):
#         if (i%2!=0 and j%2!=0) or (i%2==0 and j%2==0):
#             print("•",end="\t")
#         else:
#             print("°",end="\t")
#     print()

        #密码登录

        #countine：中断本次循环，直接进入下一次循环
i=1
while i==1:
    name=input("输入用户名：")
    password=input("输入密码:")
    if(name=="admin" and password=="666888"):
        i=0
    elif(name=="zhangsan" and password=="123456"):
        i=0
    else:
        print("用户名或密码错误，请重新输入")
print("输出成功")