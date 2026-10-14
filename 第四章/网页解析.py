# lxml 是一个高性能的HTML XML文档的解析库 支持基于xpath语法来解析和获取网页数据
# xpath 是一种文档中导航或定位元素的查询语言 让你能够准确的定位文档中的特定元素 属性和文本
from lxml import html

#读取html文件
"""
'r'：Read（读）。只读取文件内容，不能修改。这是默认模式。

'w'：Write（写）。写入内容。⚠️ 注意：如果文件已存在，会清空原内容重新写！

'a'：Append（追加）。在文件末尾追加内容，不会清空原文件。

'rb' / 'wb'：以二进制模式读写（常用于图片、视频、PDF）。

encoding 参数：
处理中文时，必须指定编码，通常用 'utf-8'。如果不写，Windows 系统默认用 GBK，很容易乱码或报错。
"""
with open("resourse/deepseek提供.html","r",encoding="utf-8") as f:
    html_txt = f.read()
    doc=html.fromstring(html_txt)#将文本字符串解析为一个文档
    #利用xpath语法 定位数据位置
    title_txt=doc.xpath("//div/h3[@class='video-title']/text()")[0]
    # xpath里的是列表
    print(title_txt)
    total_txt=doc.xpath("//div/h3/text()")
    """
    XPath 常用表达式速查表

    表达式            描述                          样例
    /                 从根节点的直接子元素          /html/body/div/h1
    //                从任意位置选择节点            //h1
    .                 当前节点下查找                ./a 与 .//a
    [n]               选择第n个元素                 //p[2]
    [last()]          选择最后一个元素              //p[last()]
    [@attr]           选择有该属性的元素            //p[@color]
    [@attr='value']   选择该属性值等于指定值的元素  //p[@color='red']
    *                 匹配任何元素节点              //body/div/*
    @*                匹配元素的任何属性            //body/div/a/@*
    text()            获取文本内容                  //div/p/text()
    """