"""
地基 3：提示词加载器
============================================================
解决什么问题？
  系统提示词写在 Python 字符串里，改一句话就得改代码；提示词一长，
  代码里全是转义和缩进，没法维护。改提示词的人通常不是写代码的人。
  现在提示词单独放 prompts/agent_prompt.txt，本文件负责读出来。
  文件不存在时给一句"人话报错"，直接告诉你缺哪个绝对路径、该改哪个配置项。

对应原项目：main/prompt_loader.py（原项目按类型分了三个 loader，本课只需要一个）
"""

import os

from config import config
from logger import get_logger
from path_tool import get_abs_path

logger = get_logger()


def load_agent_prompt() -> str:
    """从 prompts/ 目录读系统提示词，返回去掉首尾空白的字符串。"""
    # 路径来自 config.yml 的 prompt_path，不写死
    prompt_path = get_abs_path(config["prompt_path"])

    if not os.path.exists(prompt_path):
        # 关键：报错要能直接照着改，而不是甩一个 FileNotFoundError 堆栈
        message = (
            f"找不到提示词文件：{prompt_path}\n"
            f"  请检查 config.yml 里的 prompt_path 配置；\n"
            f"  并确认 prompts/ 目录下存在该文件。"
        )
        logger.error(message)
        raise FileNotFoundError(message)

    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read().strip()


if __name__ == "__main__":
    print("读到的提示词前 60 个字：")
    print(load_agent_prompt()[:60], "……")