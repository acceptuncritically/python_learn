import os
import hashlib

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter #递归文本分割器
import config_data as config
from langchain_chroma import Chroma
ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")

embeddings = OpenAIEmbeddings(
    model="embedding-3",  # 智谱的嵌入模型
    openai_api_key=ZHIPU_API_KEY,
    openai_api_base="https://open.bigmodel.cn/api/paas/v4",
)
def get_string_text(input_str:str):
    #将传入的字符串转换为md5字符串
    #将字符串转换为bytes字节数组
    str_bytes=input_str.encode("utf-8")
    #创建md5对象
    md5_obj=hashlib.md5()
    md5_obj.update(str_bytes)   #更新内容（传入将要转换的字节数组）
    md5_res=md5_obj.hexdigest()  #返回md516进制字符串
    return md5_res
def check_text(md5_str:str):
    #用来检查文件内容md5字符串是否已经被处理过了
    if not os.path.exists(config.md5_path):
        open(config.md5_path,"w",encoding="utf-8").close()
        return False
    else:
        for line in open(config.md5_path,"r",encoding="utf-8").readline():
            line=line.strip()   #处理字符串前后的空格
            if line ==md5_str:
                return True
        return False
def save_text(md5_str:str):
    #用来保存文件内容md5字符串
    with open(config.md5_path,"a",encoding="utf-8") as f:
        f.write(md5_str+"\n")
class KnowledgeBase(object):
    def __init__(self):

        os.makedirs(config.persist_directory, exist_ok=True)
        self.chroma=Chroma(
            collection_name=config.collection_name,
            embedding_function=OpenAIEmbeddings(model="embedding-3", openai_api_key=ZHIPU_API_KEY, openai_api_base="https://open.bigmodel.cn/api/paas/v4"),
            persist_directory=config.persist_directory,#数据库本地存储文件夹
        )        #chroma向量库
        self.spliter=RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
            separators=config.separator,
            length_function=len
        )       #分段器
    def unload_by_str(self,data,filename):
        """将传入的字符串进行向量化，存入向量数据库中"""
        #先得到获取数据的md5值
        md5_str=get_string_text(data)
        if check_text(md5_str):
            print("文件内容已存在，不再处理")
            return
        if len(data)>config.split_length:
            knowledge:list[str]=self.spliter.split_text(data)
        else:
            knowledge:list[str]=[data]
        metadata={filename:md5_str}
        self.chroma.add_texts(
            metadata=[metadata for i in knowledge],
            texts=knowledge
        )
        save_text(md5_str)
        return "文件内容已处理"  
if __name__ == '__main__':
    #md5保证无论数据大小都保证长度是32位的16进制
    standard=KnowledgeBase()
    while True:
        print("停止输入请输入 'stop'")
        data=input("请输入数据：")
        if data=="stop":
            break
        standard.unload_by_str(data,"test")
