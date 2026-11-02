from langchain_community.document_loaders import CSVLoader
loader=CSVLoader(
    file_path="./resourse/student.csv",
    csv_args={
        "delimiter": ",",  #指定分隔符
        "quotechar": "'",   #指定引号
        #如果原本数据有表头 就不写下面的代码 如果没有可以使用
        "fieldnames": ["name", "age", "gender","爱好"]
    },
    encoding="utf-8"
)
#批量加载数据
data=loader.load()
#懒加载
for document in loader.lazy_load():
    print(document)
    
