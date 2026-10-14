# CSV 是一种简单通用的文本文件格式，用于存储表格数据，可以直接用EXCEl打开
#csv操作 方式一
#写入
# with open("csv_data/01.csv","w",encoding="utf-8") as f:
#     f.write("姓名,性别,年龄\n")
#     #在其中用单引号来使得多种在一个单元格内
#     f.write("哥伦比亚,女,'18,20'\n")
#     f.write("芦思岩,女,18\n")
#     f.write("桑多涅,女,200\n")
# #读取
# with open("csv_data/01.csv","r",encoding="utf-8") as f:
#     for i in f:
#         print(i.strip())#strip() 表示自动去除两侧空白

#方式二 操作数据比较简单 基本用这种
import csv
with open("csv_data/02.csv","w",encoding="utf-8",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=["姓名","性别","年龄"])
    writer.writeheader()#写入表头
    writer.writerow({"姓名":"哥伦比亚","性别":"女","年龄":"18,20"})
    writer.writerow({"姓名":"桑多涅","性别":"女","年龄":"200"})
    writer.writerow({"姓名":"芦思岩","性别":"女","年龄":"18"})
#读取
with open("csv_data/02.csv","r",encoding="utf-8",newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row) 