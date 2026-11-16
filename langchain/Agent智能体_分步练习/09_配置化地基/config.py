"""
地基 2：配置读取
============================================================
解决什么问题？
  上一课里模型名、temperature、数据路径是直接写在 .py 里的：想换模型、调温度，
  就得改代码，改错了还得改回来，代码和配置搅在一起。
  现在这些值都搬进 config.yml，本文件负责把它读成一个全局字典 config：
      config["model"]          -> "deepseek-chat"
      config["temperature"]    -> 0.3
  其他文件只要 `from config import config` 就能用，再也不用打开 main.py 改字符串。

对应原项目：main/config_handler.py（原项目把 4 个 yml 拆开读，本课合成了一个 config.yml）
"""

import yaml

from path_tool import get_abs_path


def load_config() -> dict:
    """读本关文件夹下的 config.yml，返回字典。"""
    # 用 get_abs_path 而不是 "config.yml"：保证从任何目录运行都读到同一份配置
    config_path = get_abs_path("config.yml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


# 模块级全局字典：import 的时候只读一次文件，之后大家共用
config = load_config()


if __name__ == "__main__":
    print("读到的配置：", config)