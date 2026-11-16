r"""
第 09 关：配置化地基 —— 配置、提示词、路径、日志
============================================================
上一课的模型名、路径、提示词都写死在 main.py 里。能跑，但没法维护：
要换模型就改代码、换个目录运行就找不到文件、出了问题只能加 print。

本关把这四件事各拆成一块地基，main.py 只负责"组装"：
  config.py        -> 读 config.yml（模型名、temperature、各种路径）
  path_tool.py     -> 用 __file__ 算绝对路径，跟你在哪个目录运行无关
  prompt_loader.py -> 从 prompts/agent_prompt.txt 读系统提示词
  logger.py        -> 控制台 INFO + 文件 DEBUG，按天写 log/YYYY-MM-DD.log

运行：cd 到本文件夹，然后 & $py main.py
      也可以从上一级目录运行：& $py .\09_配置化地基\main.py
"""

import csv
import os
from datetime import datetime

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek

# 下面这一排 import 就是"地基"：每个文件只管一件事
from config import config
from logger import get_logger
from path_tool import get_abs_path, get_project_root
from prompt_loader import load_agent_prompt

logger = get_logger()


def load_records() -> list[dict]:
    """读 data/records.csv 成列表，每行一个 dict。路径来自配置，不写死。"""
    records_path = get_abs_path(config["records_path"])
    # DEBUG 只写进日志文件，不会在控制台刷屏——这就是"文件更详细"的用处
    logger.debug(f"正在读取数据文件：{records_path}")
    with open(records_path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@tool(description="查询指定用户在指定月份的使用记录。user_id 如 '1002'，month 如 '2025-02'，返回一段中文记录文本")
def get_user_record(user_id: str, month: str) -> str:
    """工具内部做三件事：记日志、读文件、查数据。"""
    # 工具调用日志：谁在什么时候用什么参数调了工具，出问题一眼能查到
    logger.info(f"[工具调用] get_user_record(user_id={user_id!r}, month={month!r})")

    records = load_records()
    for row in records:
        if row["用户ID"] == user_id and row["月份"] == month:
            text = (
                f"用户{user_id} {month}：户型{row['户型']}，地面{row['地面']}，"
                f"覆盖率{row['覆盖率']}，日均清扫{row['日均清扫']}，"
                f"耗材{row['耗材状态']}，对比{row['对比']}"
            )
            logger.info(f"[工具返回] {text}")
            return text

    logger.warning(f"[工具未命中] 用户{user_id}在{month}没有记录")
    return f"没有找到用户 {user_id} 在 {month} 的使用记录"


def main():
    # ① 路径地基：故意打印根目录，证明它不受 cwd 影响
    print("=" * 60)
    print("我的项目根目录是：", get_project_root())

    # ② 配置地基：模型名、温度、数据路径全部来自 config.yml
    print("=" * 60)
    print(f"配置里的模型：{config['model']}，temperature：{config['temperature']}")
    print(f"配置里的数据路径：{config['records_path']}")
    print(f"转成绝对路径：{get_abs_path(config['records_path'])}")

    # ③ 提示词地基：系统提示词从文件读，改一行字不用碰 .py
    print("=" * 60)
    system_prompt = load_agent_prompt()
    print(f"提示词文件前 40 个字：{system_prompt[:40].replace(chr(10), ' ')}……")

    # ④ 组装：用配置造模型，用提示词当 system_prompt，把工具注册进去
    agent = create_agent(
        model=ChatDeepSeek(
            model=config["model"],
            temperature=config["temperature"],
        ),
        tools=[get_user_record],
        system_prompt=system_prompt,
    )

    question = "帮我看看用户 1002 在 2025-02 的使用记录，表现怎么样？"
    print("=" * 60)
    print(f"❓ 用户：{question}")

    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    final_answer = result["messages"][-1].content

    print("-" * 60)
    print("💬 Agent 回答：")
    print(final_answer)

    # ⑤ 日志地基：告诉你这次的日志写到哪个文件，方便课后去翻
    print("=" * 60)
    log_file = os.path.join(
        get_abs_path(config["log_dir"]),
        f"{datetime.now().strftime('%Y-%m-%d')}.log",
    )
    print(f"本次日志文件：{log_file}")
    print(f"提示：日志文件里还有 {config['records_path']} 的绝对路径等 DEBUG 信息。")


if __name__ == "__main__":
    main()