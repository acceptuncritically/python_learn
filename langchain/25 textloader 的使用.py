#RecursiveCharacterTextSplitter 递归字符文本分割器 主要用于按自然段落分割大文档
# 是langchain官方推荐的默认字符分割器 他在保持上下文完整性和控制片段大小之间实现了良好平衡
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
#获得加载器对象
loader=TextLoader(
    file_path="./resourse/介绍.txt",
    encoding="utf-8",   # 指定文件编码格式
)
documents=loader.load()
#获得分割器对象
splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,  # 每个片段的最大字符数
    chunk_overlap=20,  # 相邻片段之间的重叠字符数
    #文本分段依据
    separators=["\n\n","\n" " ", "",],
    #字符统计依据
    length_function=len,
)
#将加载后的大文档通过分割器变成小文档
split_documents=splitter.split_documents(documents)
for document in split_documents:
    print(document)