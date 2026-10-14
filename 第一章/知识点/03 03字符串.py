# 字符串是字符的容器，字符串无法修改，有序，可迭代
# 字符串每一个元素都有其对应的下标
# 切片与列表相同，步长如果是-1表示从后向前
s="hello-python"
print(s[6:13])
#s[-7]="x"   出错
print(s[5:0:-1])# 步长为负数时，要反过来写
# 无法修改字符串里的值
"""
find()    查找字串，返回第一次出现的位置，找不到返回-1              s.find('python')
count()   统计字串在字符串中的次数                             s.count('H')
upper()   所有字母换成大写                                  s.upper()
lower()    所有字母换成小写                                 s.lower()
spilt()    将字符串按分隔符分割成列表                         s.spilt(' ')
strip()     去除两端的空白或指定符号                          s.strip() /s.strip('*')
replace()    将字符串中指定的字串替换成新的并作为新字符串输出    s.replace('H','c')
startswith()  检查字符串是否以指定子串开头，返回布尔值      s.startswith('p')
list 强制转换为一个个元素                                     list1=list(s)
"""
