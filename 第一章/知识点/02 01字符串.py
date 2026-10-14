# 字符串的三种定义  单引号定义  双引号定义  三引号定义（多行）
s1="hello"
s2='world'
ss="""hello world
hello python
"""
# 转义字符  \'  \"  \n  \t(tab)
msg='it\'s very easy'
print(msg)
print(ss)
#字符串也可以进行拼接  用加号拼接
s3="人生苦短"
s4="我用python"
print(s1+","+s2)#(" " 或者''都可以)
#练习  将int 类型的数字转换为字符串 str（符号）
name="涛"
age=18
pro="计算机"
print("我是"+name+",今年"+str(age)+"岁,从事"+pro)
#字符串格式化：方式一，用%s替代位置
print("我是%s,今年%s岁,从事%s"%(name,age,pro))
#方式二  可以用过  f"内容{变量/表达式}"
print(f"我是{name},今年{age}岁,从事{pro}")


