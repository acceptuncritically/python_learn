#输入10个数字，存储到一个列表，将列表排序，输出最大值最小值和平均值
# a=0
# s=[]
# while a<10:
#     num=int(input("输入数字："))
#     a=a+1
#     s.append(num)
# s.sort()
# print(s[0],end=" ")
# print(s[9],end=" ")
# b=(s[0]+s[9])/2
# print(b)

#合并两个列表中的元素，并对合并的结果进行去重处理
list1=[19,23,54,64,875,20,109,232,123,54]
list2=[55,80,72,35,60,123,54,29,91]
#合并列表
"""
 解包操作：将列表这类容器，解开成一个一个独立的元素
组包，将多个值组合成到一个容器
        
num_list=[*list1,*list2]
        print(num_list)
 list3=list1 +list2
 """
for j in list2:
    list1.append(j)
list1.sort()
print(list1)
list3=[]
for i in list1:
    if i not in list3:   #in 判定元素是否在列表中
        list3.append(i)
print(list3)
#生成1——20的平方列表
#########################
# 列表推导式 按照一定顺序快速生成一个列表的方法
# 格式一  [要插入的值 for i in 序列列表 ]
new_list2=[i**2 for i in range(1,21)]
print(new_list2)
# 格式二 [要插入的值 for i in 序列列表  if条件]
#################################
s=[]
for i in range(1,21):
    i=i*i
    s.append(i)
print(s)
#从如下数字列表中提取所有偶数，并计算其平方
new_list=[19,23,54,64,87,20,109,232,123,43,26,55,72]
s=[]
for q in new_list:
    if q %2==0:
        q=q*q
        s.append(q)
    s.sort()
print(s)
