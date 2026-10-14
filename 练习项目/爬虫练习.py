# 将网站内容 爬取并生成 折线图 柱状图 饼状图
import requests
from lxml import html
import matplotlib.pyplot as plt
import csv
from matplotlib.axes import Axes
import pandas as pd
title_URL="https://www.scrapethissite.com/pages/forms"
response = requests.get(title_URL)
doc = html.fromstring(response.text)
titles=doc.xpath("//tr[@class='team']")
# new_title = [item.strip() for item in title]
with open("../第五章/csv_data/爬虫练习.csv", "w", newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=["队名","时间","胜场","败场","胜率","进球数","失球数"])
    writer.writeheader()
    cnt=0
    for title in titles:
        cnt+=1
        writer.writerow({
            "队名": title.xpath("normalize-space(.//td[@class='name'])"),
            "时间": title.xpath("normalize-space(.//td[@class='year'])"),
            "胜场": title.xpath("normalize-space(.//td[@class='wins'])"),
            "败场": title.xpath("normalize-space(.//td[@class='losses'])"),
            # "胜率": title.xpath("normalize-space(.//td[@class='pct text-success'])")只会抓到绿色
            "胜率":title.xpath("normalize-space(.//td[contains(@class,'pct')])"),
            "进球数": title.xpath("normalize-space(.//td[@class='gf'])"),
            "失球数": title.xpath("normalize-space(.//td[@class='ga'])"),
        })
        # XPath内置的normalize - space()会自动去掉首尾空格、把中间的连续空白压成一个空格，
        # 而且直接返回字符串，不是列表。这样就不用[0].strip()了。
        print(f"第{cnt}支队伍的数据已存放完成")
print("存放完成")
df=pd.read_csv("../第五章/csv_data/爬虫练习.csv",usecols=["队名","时间","胜场","败场","胜率","进球数","失球数"])
plt.rcParams['font.sans-serif'] = ['SimHei']
figure,axes=plt.subplots(nrows=2, ncols=2, figsize=(20,10))
axes1: Axes=axes[0,0]
axes2: Axes=axes[1,0]
axes3: Axes=axes[0,1]
axes4: Axes=axes[1,1]
axes1.set_title("各队伍胜场数",fontsize=20)
axes1.set_xlabel("队名",fontsize=20)
axes1.set_ylabel("胜场数",fontsize=20)
axes1.bar(df["队名"],df['胜场'],color="darkblue",width=0.3)
axes1.tick_params(axis='x', rotation=90, labelsize=8)
axes1.grid("--")

axes3.pie(df["胜率"],labels=df["队名"].str[0:4],center=(0,-5),radius=1)

plt.show()
