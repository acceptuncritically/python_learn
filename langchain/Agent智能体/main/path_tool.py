#Agent日志保留和路径开发
"""
为整个过程提供统一的绝对路径
"""
import os
def get_project_root()->str:
    """
    获取工程所在的目录
    :return: 字符串
    """
    #当前文件的绝对路径
    current_file=os.path.abspath(__file__)
    #获取工程的根目录,先获得所在文件夹的路径
    current_dir=os.path.dirname(current_file)
    #获取工程的根目录
    current_root=os.path.dirname(current_dir)
    return current_root
def get_abs_path(relative_path:str)->str:
    """
    获取绝对路径
    :param relative_path: 相对路径
    :return: 绝对路径
    """
    current_root=get_project_root()
    return os.path.join(current_root,relative_path)
if __name__ == '__main__':
    print(get_project_root())
    print(get_abs_path('log/log.txt'))

