import logging
import os
from datetime import datetime
from main.path_tool import get_abs_path
"""
1.保存日志所在位置的根目录,并确保根目录存在，如果不存在则创建在本文件的同级目录下
2.保证日志格式
3.定义函数参数为，创建logger实例的名称，控制台日志级别，文件日志级别，日志文件路径
4.设置logger对象获取日志的等级
5.配置控制台和文件的handler，以及设置handler的等级和格式    
    Logger 自己不会输出任何东西。它只是个“分发器”，必须挂上至少一个 handler，日志才有出口
"""
#日志保存的根目录
LOG_ROOT =get_abs_path('log')
#确保日志的目录存在,如果不存在则创建在本文件的同级目录下
os.makedirs(LOG_ROOT,exist_ok=True)
#日志格式
DEFAULT_LOG_FORMAT = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')
"""
常用 logging 格式字段：

%(asctime)s     时间          %(levelname)s   日志级别，如 INFO/WARNING/ERROR
%(name)s        logger 名称   %(message)s     日志内容
%(filename)s    文件名         %(lineno)d      行号
%(funcName)s    函数名         %(module)s      模块名
%(process)d     进程 ID       %(threadName)s  线程名
""""""
常用 logging 格式字段：

%(asctime)s     时间           %(levelname)s   日志级别，如 INFO/WARNING/ERROR
%(name)s        logger名称     %(message)s     日志内容
%(filename)s    文件名         %(lineno)d      行号
%(funcName)s    函数名         %(module)s      模块名
%(process)d     进程 ID        %(threadName)s  线程名
"""
def get_logger(
        name="agent",
        console_level=logging.INFO,
        file_level=logging.DEBUG,
        log_file=None
):
    #获取或创建一个名为 name 的 Logger 对象，当 name 存在时，返回该 Logger 对象，否则创建一个新的 Logger 对象
    logger = logging.getLogger(name)
    #设置这个 Logger 对象的最低日志门槛级别 保证debug以上的日志都能够记录
    logger.setLevel(logging.DEBUG)
    #避免重复添加handler
    #配置一个控制台的handler
    if logger.handlers:
       return logger
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(DEFAULT_LOG_FORMAT)
    logger.addHandler(console_handler)#将handler挂到logger上
    #配置一个文件的handler
    if not log_file:
        log_file = os.path.join(LOG_ROOT,f"{name}_{datetime.now().strftime('%Y-%m-%d')}.log")
    file_handler = logging.FileHandler(log_file,encoding="utf-8")
    file_handler.setLevel(file_level)
    file_handler.setFormatter(DEFAULT_LOG_FORMAT)
    logger.addHandler(file_handler)#将handler挂到logger上
    return logger
logger = get_logger()

