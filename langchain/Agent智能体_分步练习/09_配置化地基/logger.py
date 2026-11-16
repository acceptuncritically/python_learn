"""
地基 4：日志
============================================================
解决什么问题？
  出了问题只能靠 print 猜：哪一步、几点、哪行代码出错？print 还只能给人看，
  程序关掉就什么都没了。
  本文件配置一个 logger，同一条日志发给两个出口（handler）：
    · 控制台：只显示 INFO 及以上（干净，不刷屏）
    · 文件  ：连 DEBUG 都记（详细，事后查问题）
  日志文件放在 log/YYYY-MM-DD.log，每天一个，按天自动分开。

对应原项目：main/log_handler.py（原项目多传了几个参数，本课简化成固定 INFO/DEBUG）
"""

import logging
import os
import sys
from datetime import datetime

from config import config
from path_tool import get_abs_path

# 日志目录也来自配置；不存在就建出来（第一次运行时 log/ 是自动生成的）
LOG_DIR = get_abs_path(config["log_dir"])
os.makedirs(LOG_DIR, exist_ok=True)

# 日志格式：时间 | 级别 | 哪个文件第几行 | 内容
LOG_FORMAT = logging.Formatter(
    "%(asctime)s | %(levelname)-7s | %(filename)s:%(lineno)d | %(message)s"
)


def get_logger(name: str = "practice") -> logging.Logger:
    """拿到一个同时往控制台和文件写日志的 logger。"""
    logger = logging.getLogger(name)
    # 总闸门开到最松（DEBUG），具体显示多少交给下面的 handler 决定
    logger.setLevel(logging.DEBUG)

    # 防止重复添加 handler：重复添加会让同一条日志被打印两遍
    if logger.handlers:
        return logger

    # 出口 A：控制台，只看 INFO 及以上
    # 默认写 stderr，这里明确指定 stdout：PowerShell 里输出顺序更整齐
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(LOG_FORMAT)
    logger.addHandler(console_handler)

    # 出口 B：文件，DEBUG 也记，按天一个文件
    log_file = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(LOG_FORMAT)
    logger.addHandler(file_handler)

    return logger


if __name__ == "__main__":
    # 单独运行：验证"控制台看不到 DEBUG，但文件里有"
    logger = get_logger()
    logger.debug("这是一条 DEBUG，只应该出现在日志文件里")
    logger.info("这是一条 INFO，控制台和文件都应该有")
    print("日志目录：", LOG_DIR)