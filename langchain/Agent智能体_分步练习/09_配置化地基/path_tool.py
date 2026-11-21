"""
地基 1：路径工具
============================================================
解决什么问题？
  代码里写 "data/records.csv" 这种相对路径时，它是相对"当前工作目录"（cwd）算的。
  在 A 文件夹运行能找到，换到 B 文件夹运行就找不到——所谓"换个目录就报错"。
  get_project_root() 用 __file__ 定位本文件自己的位置，再往上找带 config.yml 的目录，
  于是不管你在哪个目录敲 python，算出来的根目录都一样。

对应原项目：main/path_tool.py
"""

import os


def get_project_root() -> str:
    """返回本关文件夹（存放 config.yml 的那个目录）的绝对路径。"""
    # __file__ 是当前 .py 文件的路径；abspath 把它变成绝对路径
    # os.path.dirname()表示取目录部分，从字符串末尾往前找最后一个分隔符，把后半段砍掉,就是绝对路径中将当前文件名删去

    # os.path.basename()表示取文件名部分，在绝对路径中将目录部分删去
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 从当前文件所在目录开始，一层层往上找，谁有 config.yml 谁就是"项目根"
    while True:
        if os.path.exists(os.path.join(current_dir, "config.yml")):
            return current_dir
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:  # 已经到盘符根目录（如 E:\），还没找到
            raise RuntimeError(
                "找不到项目根目录：从本文件往上，没有任何一层目录包含 config.yml"
            )
        current_dir = parent_dir


def get_abs_path(relative_path: str) -> str:
    """把相对路径拼成基于项目根目录的绝对路径。"""
    # os.path.join 拼出来的本来就用本机分隔符。normpath 真正的作用是规范化——清掉多余的斜杠、解析 . 和 ..
    return os.path.normpath(os.path.join(get_project_root(), relative_path))


if __name__ == "__main__":
    # 单独运行本文件可以自测：这两个输出在任何目录运行都一样
    print("项目根目录：", get_project_root())
    print("数据文件绝对路径：", get_abs_path("data/records.csv"))