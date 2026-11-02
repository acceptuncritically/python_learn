from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader(
    file_path="./resourse/填写说明.pdf",
    mode="page",        #读取模式，可选page：按照页面划分不同的document 和single：返回单个document包含整个pdf数据

    #password="password",  #密码，如果pdf有密码则需要输入

)
i=0
for document in loader.lazy_load():
    i+=1
    print(document)
    print("="*30,i)
