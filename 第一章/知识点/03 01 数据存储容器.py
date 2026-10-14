#列表
s=[54,15,75,108,"A","hello",True]
#元素有序，可以重复，元素可被修改，可以存储不同类型的元素
#可以反向索引 最后一位为-1 向前-2 ，-3...
print(type(s))

#获取
print(s[0])
print(s[-7])

#修改
s[2]="B"
print(s)   #能够直接输出整个列表

#删除

del s[4]
print(s)
#遍历
for x in s:
    print(x)

        #切片 序列数据[开始索引：结束索引：步长 ]
    #不包含结束索引的书，结束索引未指定默认为整个列表
    #步长默认为1
s=["A","B","C","D","E"]
a=s[0:4:1]

print(a)
print(s[0::2])
#步长默认为一时，可以简化为s[:5]==>s[0:5:1]


#常用方法
# append()  在尾部添加元素  s.append(1)
# insert()  在指定索引之前插入该元素 s.insert(0,92)
# remove()  移除列表中匹配到第一个值 s.remove(75)
# pop()   删除指定索引位置的数，默认为最后一个 s.pop()或者s.pop() 可以用变量接取这个返回值
# sort()  对数据类型一致的元素进行排序 s.sort()
# reverse()  反转列表元素 s.reverse()
"""
reverse() 示例

lista = [1, 2, 3, 4]
lista.reverse()
print(lista) # 输出: [4, 3, 2, 1]
复制
reverse() 方法直接修改原列表，返回值为 None。
"""