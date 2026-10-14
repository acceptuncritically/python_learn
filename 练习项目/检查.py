import requests
from lxml import html
import csv
import re
import pandas as pd
target_URL='https://books.toscrape.com'
response=requests.get(target_URL)
doc=html.fromstring(response.text)

# 1. 找到每一本书的父级容器（一个 <article> 标签代表一本书）
books = doc.xpath('//article[@class="product_pod"]')
last_URl=doc.xpath("//article[@class='product_pod']//a/@href")
with open("../第五章/csv_data/检查.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["书名", "价格", "星级","储存"])
    writer.writeheader()
    # 2. 遍历每一本书
    cnt=0
    for book in books:
        comment_URl=target_URL+'/'+last_URl[cnt]
        cnt+=1
        response1=requests.get(comment_URl,timeout=5)
        doc1=html.fromstring(response1.text)
        stock=doc1.xpath("//p[@class='instock availability']/text()")
        # 2. 使用正则提取第一个连续的数字
        New_Stock = re.search(r'\d+', str(stock))
        # 在这个书的局部里面找书名
        title = book.xpath('.//h3/a/@title')[0]
        # 找价格 (注意 .// 表示在当前节点内找)
        price = book.xpath('.//p[@class="price_color"]/text()')[0]
        _price=re.search(r'\d+.\d+', str(price))
        # 找星级 (class 类似 "star-rating Three")
        star_class = book.xpath('.//p[contains(@class, "star-rating")]/@class')[0]
        star = star_class.replace("star-rating ", "")  # 把 "star-rating " 去掉，只留 "Three"
        # 3. 写入一行
        writer.writerow({
            "书名": title,
            "价格": _price.group(),
            "星级": star,
            "储存": New_Stock.group()
        })
        print(f"已成功输入第{cnt}本书")
print("完整数据写入完毕！")
# import pandas as pd
# csv_path = r"C:\你的路径\input.csv"
# excel_path = r"C:\你的路径\output.xlsx"
# df = pd.read_csv(csv_path, encoding="utf-8-sig")
# df.to_excel(excel_path, index=False, engine="openpyxl")
# print("转换完成：", excel_path)
import matplotlib.pyplot as plt
df=pd.read_csv("../第五章/csv_data/检查.csv", usecols=["价格", "星级", "储存"])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(10,5))
plt.bar(df["星级"],df["储存"],color="darkblue",width=0.3)
plt.title("柱状图",fontsize=20)
plt.xlabel("星级",fontsize=20)
plt.ylabel("数量",fontsize=20)
plt.grid("--",alpha=0.3)
plt.show()




