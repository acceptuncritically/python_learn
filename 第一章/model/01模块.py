"""

Python 模块导入方式（注释版）：
1. import 模块名
   示例：import random, os
   调用：模块名.功能名
   调用示例：random.randint(10, 100)

2. import 模块名 as 别名
   示例：import random as rd
   调用：别名.功能名
   调用示例：rd.randint(10, 100)

3. from 模块名 import 功能名
   示例：from random import randint, choice
   调用：功能名
   调用示例：randint(10, 100)
   from random import (
    randint,
    choice,
    shuffle,
    sample,
    uniform
)

4. from 模块名 import 功能名 as 别名
   示例：from random import randint as rint
   调用：别名
   调用示例：rint(10, 100)

5. from 模块名 import *
   示例：from random import *
   调用：功能名
   调用示例：randint(10, 100)
    from 模块名 import *：把某个模块里的所有东西（函数、类、变量）全部“倒”进你当前的代码文件里
"""
# import random
# for i in range(1,100):
#     a=random.randint(1,100)
#     print(a)

from random import randint
for i in range(1,100):
    a=randint(1,100)
    print(a)