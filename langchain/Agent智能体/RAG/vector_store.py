from langchain_chroma import Chroma
from main.config_handler import chroma_config
from model.factory import embedding_model, chat_model
from langchain_text_splitters import RecursiveCharacterTextSplitter
from main.path_tool import get_abs_path
from main.file_handler import pdf_loader, text_loader,listdir_with_allowed_type
import os
from main.log_handler import logger
import hashlib  # 记得在文件最上面加上这个导入
class VectorStoreService:
    def __init__(self):
        self.vector_store=Chroma(
            collection_name=chroma_config["collection_name"],
            embedding_function=embedding_model,
            persist_directory=chroma_config["persist_direct"],
        )
        self.spliter=RecursiveCharacterTextSplitter(
            chunk_size=chroma_config["chunk_size"],
            chunk_overlap=chroma_config["chunk_overlap"],
            separators=chroma_config["separator"],
            length_function=len,
        )
    def get_retriever(self):
        return self.vector_store.as_retriever(search_kwargs={"k":chroma_config["k"]})



    def load_document(self):
        """
        从数据文件夹中读取数据文件，转为向量存入向量库
        要计算文件的md5去重
        """
        # 1. 真正的计算文件 MD5 的方法
        def get_file_md5_hex(file_path: str):
            if not os.path.isfile(file_path):
                return ""
            with open(file_path, "rb") as f:
                md5_obj = hashlib.md5()
                md5_obj.update(f.read())
                return md5_obj.hexdigest()

        def check_md5_hex(md5_for_check: str):
            md5_file_path = get_abs_path(chroma_config["md5_hex_store"])
            if not os.path.exists(md5_file_path):
                open(md5_file_path, "w").close()
                return False
            with open(md5_file_path, "r", encoding="utf-8") as f:
                for line in f.readlines():
                    if line.strip() == md5_for_check:
                        return True
            return False

        def save_md5_hex(md5_to_save: str):
            with open(get_abs_path(chroma_config["md5_hex_store"]), "a", encoding="utf-8") as f:
                f.write(md5_to_save + "\n")

        # 2. 根据文件后缀读取内容的方法
        def load_file_content(file_path: str):
            if file_path.endswith(".txt"):
                return text_loader(file_path)
            if file_path.endswith(".pdf"):
                return pdf_loader(file_path)
            return []

        allowed_files_path = listdir_with_allowed_type(
            chroma_config["allow_knowledge_path"],
            chroma_config["allow_knowledge_file_type"]
        )

        print(f"【扫描到的文件】: {allowed_files_path}")  # 调试用，看看有没有扫到文件

        for path in allowed_files_path:
            # 计算真实文件的 MD5
            file_md5 = get_file_md5_hex(path)

            if check_md5_hex(file_md5):
                logger.info(f"文件{path}已存在，跳过添加")
                continue

            try:
                # 读取文件内容
                documents = load_file_content(path)

                if not documents:
                    logger.warning(f"[加载知识库]{path}内没有有效文本内容，跳过")
                    continue

                split_document = self.spliter.split_documents(documents)

                if not split_document:
                    logger.warning(f"[加载知识库]{path}分片后没有有效文本内容，跳过")
                    continue

                # 将内容存入向量库
                self.vector_store.add_documents(split_document)

                # 记录这个已经处理好的文件的md5
                save_md5_hex(file_md5)

                logger.info(f"[加载知识库]{path} 内容加载成功")

            except Exception as e:
                logger.error(f"[加载知识库]{path}加载失败：{str(e)}", exc_info=True)
                continue

if __name__=="__main__":
    # 加上这三行调试
    from main.path_tool import get_abs_path
    path = get_abs_path(chroma_config["allow_knowledge_path"])
    print(f"配置的原始路径: {chroma_config['allow_knowledge_path']}")
    print(f"解析后的绝对路径: {path}")
    print(f"这个路径在电脑上存在吗?: {os.path.exists(path)}")
    print(f"允许的文件类型: {chroma_config['allow_knowledge_file_type']}")

    vs=VectorStoreService()
    vs.load_document()
    retriever=vs.get_retriever()
    res = retriever.invoke("公司")
    print(f"检索到的结果数量: {len(res)}")
    # ... 后面的代码保持不变