        # import random
        # num = random.randint(1,100)
import random
num = random.randint(1,100)

a=int(input("请输入："))
while a!=num:
    if a>num:
        print("大了")
    elif a<num:
        print("小了")
    a = int(input("请输入："))
print("猜对了")