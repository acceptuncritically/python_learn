for i in range(1,100):
    if i%2!=0 :
        print(i)
"""
range(end) 生成一个从零开始到end结束的序列    不包含end
range(start,end)  获取一个start开始end结束的序列  不包含end
range(start,end,step) 生成一个，start开始end结束，step 步长的  不包含end
range(0,10,2)  0 2 4 6 8
"""
he=0
for i in range(102,500,3):
        he+=i
print(he)

#嵌套循环
m=int(input("长方形的长："))
n=int(input("长方形的宽："))
for m in range(1,m+1):
    print("")
    for n in range(1,n+1):
        print("* ",end="")     #print 自动换行   print("\n")换行两次   end=""表示不换行


#打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
            print(f"{i} * {j} = {i*j}",end="\t")
    print()
