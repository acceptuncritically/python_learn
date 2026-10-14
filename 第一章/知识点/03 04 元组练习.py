students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),     #元组可以混用
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t\t平均分")
# 方式一：
for s in students:
    total=s[2]+s[3]+s[4]
    avg=total/3
    print(f"{s[0]}\t {s[1]}\t {s[2]}\t\t {s[3]}\t\t{s[4]}\t\t {total}\t\t{avg:.1f}")
"""
 方式二：
 for a,b,c,d,e in students:
    total=c+d+e
    avg = total / 3
"""

#统计每一科的最高最低
chinese=[s[2] for s in students]
math=[s[3] for s in students]
english=[s[4] for s in students]
print(f"语文成绩：{min(chinese)}")
print(f"语文成绩：{max(chinese)}")
print(f"数学成绩：{min(math)}")
print(f"数学成绩：{max(math)}")
print(f"英语成绩：{min(english)}")
print(f"英语成绩：{min(english)}")
for s in students:
    total=s[2]+s[3]+s[4]
    avg=total/3
    if avg>90:
        print(f"{s[1]}")
