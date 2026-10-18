#通过yield方式 获取生成器
import math
from pathlib import Path
#定义函数存储到生成器中
#yield:
    # 创建生成器对象
    # 将值存储到生成器中
    # 返回生成器
def my_fun():
    for i in range(100):
        yield i
my_get2=my_fun()
print(type(my_get2))
# 保证了yield确实生成 为生成器

"""
案例：基于传入的数值(每批次的歌词条数)，创建 生成器，生成批次歌词.
"""

# 需求：基于文件中 周杰伦的歌词，创建生成器，根据传入的每批次的歌词条数，生成歌词批次.
def dataset_loader(batch_size):
    """
    自定义的歌词生成器
    :param batch_size:每批次的歌词条数
    :return: 生成器每个元素都是一批次的数据
    """
    # 以“脚本自身所在目录”为基准定位歌词文件，不受 PyCharm/终端工作目录影响
    current_dir = Path(__file__).resolve().parent / "歌词.txt"
    """
        from pathlib import Path
        # 1. 获取当前脚本所在目录 (即 生成器和正则表达式 文件夹)
        current_dir = Path(__file__).resolve().parent
        # 2. 获取上一级目录 (即 python_learn 文件夹)
        parent_dir = current_dir.parent
        # 3. 拼接同级目录下的文件路径
        target_path = parent_dir / "my_data" / "picture_1.png"
        # --- 测试是否找对 ---
        print(f"目标路径是: {target_path}")
        print(f"文件存在吗: {target_path.exists()}")
        # 如果存在就可以正常读取
        # with open(target_path, "rb") as f: ...
    """
    with open(current_dir, "r", encoding="utf-8") as f:
        #一次读取读取所有行
        lines=f.readlines()
        print(lines)
        total_batch=math.ceil(len(lines)/batch_size)
        #ceil向上取整
        for i in range(total_batch):
            #第一批歌词索引为index=0
            yield lines[i*batch_size:(i+1)*batch_size]
dl=dataset_loader(10)
for j in dl:
    print(j)