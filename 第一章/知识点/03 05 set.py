#存储不能重复的元素 无序  可修改    set 会自动去重
s1={"a","b","c",5,6,5}
s2=set()
print(s1)
"""
add 添加元素到集合中                                  s1.add('t')
remove   移除集合中的指定元素 指定元素不存在将报错            s1.remove('t')
pop     随机删除集合中的元素并返回                           e=s1.pop()
clear   清空集合                                         s1.clear()
difference   求取两个集合的差集 包含在第一个集合但不包含在第二个集合的元素 s1.difference(s2)
union   求取两个集合的并集            s1.union(s2)
intersection   求取两个集合的交集    s1.intersection(s2)
"""
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}

# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}

# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}

# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

#找出同时选修了法语和艺术
a=french_set.intersection(art_set)
print(a)
#找出同时选修了四门课的
b=basketball_set.intersection(football_set)
c=a.intersection(b)
print(c)
#找出选修了足球没有选秀篮球的学生
d=football_set.difference(basketball_set)
f=football_set-basketball_set
#集合推导式==>    {要往集合中添加的元素(基本和s有关) for s  in  set1  if 条件}
g={s for s in football_set if s not in basketball_set}
print(d,f,g)
#统计每一个学生的选课数量
#获取所有学生名单
all_set=basketball_set.union(football_set).union(art_set).union(french_set)
all_set1=basketball_set|football_set|art_set|french_set
print(all_set)
print(all_set1)
#统计每一个学生的选课数量
all_list=[*football_set,*art_set,*french_set,*basketball_set]

for i in all_set:
    print(f"{i}选修了{all_list.count(i)}")
