"""
=====================================================================================
导入形式                         代码样例                                  调用方式                  调用方式
=====================================================================================
import 包名.模块名               import utils.my_fun                       包名.模块名.功能名        utils.my_fun.log_separator1()
from 包名 import 模块名          from utils import my_fun                  模块名.功能名             my_fun.log_separator1()
from 包名 import *               from utils import *                       模块名.功能名             my_fun.log_separator1()
from 包名.模块名 import 功能名   from utils.my_fun import log_separator1   功能名                    log_separator1()
from 包名.模块名 import *        from utils.my_fun import *                功能名                    log_separator1()
=====================================================================================

注意：在通过 'from 包名 import *' 导入全部模块的时候，需要在 __init__.py 文件中添加 '__all__=[]'，控制允许导入的模块列表。
"""

#bao
"""
import my_fun,my_ven
my_fun.log_fun1()
print(my_ven.PI)
"""

import bao.my_fun,bao.my_ven
bao.my_fun.log_fun1()
print(bao.my_ven.PI)

from bao.my_fun import log_fun1
log_fun1()

from bao.my_ven import PI
print(PI)

from bao import *
bao.my_fun.log_fun1()
print(bao.my_ven.PI)