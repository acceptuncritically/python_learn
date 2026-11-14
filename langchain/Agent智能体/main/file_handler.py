from langchain_community.document_loaders import PyPDFLoader, TextLoader
import os
import hashlib
from main.log_handler import logger


def get_file_md5_hex(file_path):
    """
    获取文件的md5值的16进制字符串
    :param file_path:
    :return:
    """
    if not os.path.exists(file_path):
        logger.error(f"文件不存在：{file_path}")
        return None
    if not os.path.isfile(file_path):
        logger.error(f"这不是一个文件：{file_path}")
        return None
    md5_obj = hashlib.md5()
    chunk_size = 8192
    try:
        with open(file_path, "rb") as f:#防止读取过大文件溢出
            while chunk := f.read(chunk_size):
                md5_obj.update(chunk)
            """类似于do while
            chunk=f.read(8192)
            while chunk:
                md5_obj.update(chunk)
                chunk=f.read(8192)
            """
        return md5_obj.hexdigest()
    except Exception as e:
        logger.error(f"获取文件md5值出错：{e}")
        return None
# def listdir_with_allowed_type(path:str,allowed_types:tuple[str]):    #返回文件夹内的文件列表(允许的文件后缀)
#     files=[]
#     if not os.path.isdir(path):
#         logger.error(f"{path}文件夹不存在")
#         return None
#     for f in os.listdir(path):
#         if f.endswith(allowed_types):
#             files.append(os.path.join(path,f))
#     return tuple(files)
def pdf_loader(filepath:str,password:None):
    return PyPDFLoader(filepath,password).load()
def text_loader(filepath:str):
    return TextLoader(filepath,"utf-8").load()


def listdir_with_allowed_type(path: str, allowed_types):
    """返回文件夹内的文件列表(允许的文件后缀)"""
    files = []
    if not os.path.isdir(path):
        logger.error(f"{path}文件夹不存在")
        return None

    # 【关键修复】将配置传进来的列表转为元组，并处理可能缺少点的情况
    if isinstance(allowed_types, str):
        allowed_types = (allowed_types,)
    else:
        allowed_types = tuple(allowed_types)

    # 确保后缀统一带点，比如 "txt" 变成 ".txt"
    allowed_types = tuple(t if t.startswith('.') else f'.{t}' for t in allowed_types)

    print(f"DEBUG: 扫描路径 {path}，允许的后缀: {allowed_types}")  # 调试打印

    for f in os.listdir(path):
        print(f"DEBUG: 发现文件 {f}，匹配结果: {f.endswith(allowed_types)}")  # 调试打印
        if f.endswith(allowed_types):
            files.append(os.path.join(path, f))
    return tuple(files)
