# python_learn

一个 Python 学习与练习仓库，用来记录从基础语法、数据分析、网络爬虫、并发与网络编程，到数据结构与算法、LangChain 大模型应用、PyTorch 入门的学习过程。

仓库按专题分目录组织，大部分代码是可直接运行的小例子，并配有大量中文注释和笔记，适合按目录顺序阅读，也方便日常速查。目前包含 180 多个 Python 脚本。

## 目录结构

```text
python_learn/
├── 第一章/                  # Python 基础语法与练习题
├── 第三章/                  # 大模型 API 调用与 AI 应用（Streamlit / F5-TTS）
├── 第四章/                  # 网络爬虫基础（CSV、正则表达式、requests + lxml）
├── 第五章/                  # 数据分析（Jupyter + pandas + Matplotlib）
├── 第六章/                  # 面向对象高级与 FastAPI 基础
├── 第七章/                  # Python 进阶（闭包、装饰器、生成器、线程/进程、socket）
├── 算法详解/                # 复杂度、链表、二叉树、排序与二分查找
├── leetcode/                # LeetCode 练习，一题一文件
├── 深度学习+pytorch/        # PyTorch 张量、自动微分与线性回归训练
├── langchain/               # LangChain 学习脚本（提示词、LCEL、记忆、RAG 组件）
├── coze/                    # Coze 平台与 AI Agent 概念笔记
├── 练习项目/                # 面向对象、爬虫、线性回归等综合练习
├── 需要下载.py              # 依赖安装备注（pip 命令注释）
├── LICENSE
└── README.md
```

说明：

- 仓库中没有 `第二章` 目录。
- `*.py~` 文件是 PyCharm 自动生成的备份，可以忽略。
- `.venv/` 是本地虚拟环境（未纳入版本控制），`.idea/` 是 PyCharm 项目配置。

## 内容概览

### 第一章 Python 基础

从字面量、变量和运算符开始，覆盖 Python 基础语法：

- 输入输出、类型转换、算术/比较/逻辑运算符
- 字符串定义、格式化、切片与常用方法
- `if/elif/else`、`match-case` 模式匹配、`while/for` 循环
- 列表、元组、集合、字典等常用容器及推导式
- 函数定义、默认参数、`*args`/`**kwargs`、`lambda`
- 模块与包（`bao/` 为自定义包示例，`model/` 为导入示例）
- 类与对象入门
- `练习题/` 中按列表、元组、字典、字符串分类的练习

知识点按“一条一文件”拆分，部分脚本运行时需要键盘输入。

### 第三章 大模型 API 与 AI 应用

按“网络基础 → 大模型调用 → 界面 → 语音”的顺序练习：

- 网络与 HTTP 基础笔记：`AI应用/网络基础知识.py`、`AI应用/HTTP协议与请求.py`、`AI应用/大模型调用.py`
- DeepSeek API 调用：`01 deepseek 调用测试.py`
- Streamlit 入门与 AI 伴侣聊天应用：`AI应用/streamlit 入门程序.py`、`AI应用/streamlit 入门程序01.py`、`AI应用/03 AI_partner.py`、`AI应用/04 AI_partner.py`、`AI应用/05 AI_partner.py`（`session_state` 多轮对话、流式输出、侧边栏）
- 语音克隆：`AI应用/05 AI_partner 音频.py`（F5-TTS、librosa 处理参考音频）
- 素材：`AI应用/resourses/` 下的图片、视频和音频

AI 伴侣类脚本需要联网并配置 `DEEPSEEK_API_KEY`；Streamlit 应用需要用 `streamlit run` 启动。

### 第四章 网络爬虫基础

- CSV 读写：`01 实践 电影提取csv.py`（`csv.DictReader` / `DictWriter`）、`练习.py`
- 正则表达式：`正则表达式.py`（元字符、`re.findall` 提取手机号/日期）
- 网页解析：`网页解析.py`（lxml + XPath 解析本地 HTML，`resourse/deepseek提供.html` 为模拟页面）
- 爬取练习：`02 网络机器人 入门程序.py`（TIOBE 榜单）、`02 实践 电影提取.py`（TMDB 电影数据）
- 数据：`csv_data/` 下的练习 CSV

抓取脚本依赖目标站点的页面结构，运行前注意网络和工作目录。

### 第五章 数据分析

- Jupyter Notebook 使用：`01 jupyter 演练.ipynb`、`Jupyter Notebook.py`
- pandas：`pandas.ipynb`、`pandas.series.ipynb`、`读取 与保存文件.ipynb`、`数据的查看选择与过滤.ipynb`、`数据排序.ipynb`、`数据的分组.ipynb`、`数据清洗.ipynb`
- Matplotlib：`Matplotlib 入门.ipynb`、`Matplotlib 基础.ipynb`、`Matplotlib 基础实战.ipynb`、`01数据分析准备工作.ipynb`（电影数据的 2×2 统计图）
- 数据：`csv_data/` 下 7 份 CSV，包括学生信息、学生成绩、电影数据、订单数据等

在 `第五章/` 目录下启动 Jupyter 运行。

### 第六章 面向对象高级与 FastAPI

- 封装：`01面向对象 高级封装.py`
- 继承与方法重写：`02 面向对象 高级继承.py`
- 多继承：`03面向对象 高级继承--多继承.py`
- 多态：`04 面向对象高级 多态.py`
- 鸭子类型：`05面向对象高级 多态 鸭子类型.py`
- FastAPI 基础：`FastAPI基础.py`（两个 GET 接口，`uvicorn` 启动，默认 8000 端口）
- `web AI汉字迷盒.py` 为空文件，尚未完成

### 第七章 Python 进阶

- 闭包与 `nonlocal`：`闭包.py`、`nonlocal关键词.py`
- 装饰器：`装饰器.py`、`装饰器的使用.py`、`一个装饰器装饰多个函数.py`、`多个装饰器装饰一个函数.py`
- 浅拷贝与深拷贝：`浅拷贝与深拷贝.py`
- 迭代器、生成器、`property`：`生成器和正则表达式/` 下的 `迭代器.py`、`生成器 推导式.py`、`生成器yield方式.py`、`property 装饰器.py`、`property 类属性.py`
- 多线程：`线程/` 下的线程入门、线程注意点、数据共享、互斥锁等
- 多进程：`进程/` 下的多进程、传参、进程编号、数据隔离等
- socket 网络编程：`创建socket对象.py`、`网络编程.py`、`进程/服务端与客户端连接 服务端.py`、`进程/服务端与客户端连接 客户端.py`、`进程/文件上传 服务器.py`、`进程/文件上传 服务器 多线程.py`、`进程/文件上传 客户端.py`

网络编程示例需要两个终端分别启动服务端和客户端，并按本机情况修改代码中的 IP、端口和文件路径。

### 算法详解

- 复杂度与概念笔记：`大O标记法.py`、`算法讲解.py`、`数据结构讲解.py`、`顺序表.py`
- 单向链表：`链表.py`（`SingleNode` / `SingleLinkedList`，含增删改查和遍历）
- 二叉树：`二叉树/深度遍历.py`（先序/中序/后序）、`二叉树/广度遍历.py`（层次遍历）、`二叉树/反推二叉树结构.py`
- 排序：`二叉树/冒泡排序.py`、`二叉树/选择排序.py`、`二叉树/插入排序.py`、`二叉树/快速排序.py`
- 查找：`二叉树/二分查找.py`、`二叉树/二分查找递归版.py`
- 配图：`picture/`
- `KMP算法.py`、`递归.py`、`衡量算法速度.py` 为空文件，尚未补全

排序和查找代码目前放在 `二叉树/` 目录下，目录命名沿用早期结构。

### leetcode

- 一题一文件，命名为纯题号（如 `3.py`、`209.py`）、“题号 + 题名”（`1两数之和.py`）或中文题名（`移动零.py`、`最长连续数列.py`、`地雷.py`）
- 覆盖哈希表、双指针/滑动窗口、前缀和、差分数组、二分查找、区间合并、矩阵模拟等常见题型
- `method.py` 收集了常见解题模板
- 多数文件末尾带简单样例调用，部分文件只有函数或类定义

### 深度学习 + PyTorch

- PyTorch 简介：`pytorch简介.py`
- 张量基础（`张量/`，11 个脚本）：张量创建、全 0/全 1 张量、线性与随机变量、类型转换、元素运算、点乘与矩阵乘、统计函数、索引、形状操作、拼接
- 自动微分（`自动微分/`）：`自动微分.py`、`自动微分的问题.py`、`自动微分的真实应用场景.py`、`循环更新参数.py`、`激活函数.py`、`神经网络.py`
- 完整训练示例：`自动微分/模拟线性回归.py`（`TensorDataset`/`DataLoader` + `nn.Linear` + `MSELoss` + `SGD`，100 轮，CPU 上几秒完成并绘图）
- 参数初始化笔记：`神经网络/参数初始化.py`
- 配图：`自动微分/picture/`

这些脚本都可以在 CPU 上运行，不依赖 GPU。

### langchain

按编号组织的 LangChain 学习脚本（01–15、18–27，共 25 个），可以按顺序阅读：

- 01–04：OpenAI 兼容接口调用 DeepSeek、RAG 概念、`invoke`/`format` 的区别、JSON 处理
- 05–11：`ChatDeepSeek`、余弦相似度、多轮上下文、流式输出、few-shot 提示词、文本向量化（智谱 `embedding-3`）
- 12–15：`PromptTemplate`、`FewShotPromptTemplate`、`ChatPromptTemplate` + `MessagesPlaceholder`、LCEL 管道（`|`）
- 18–22：`StrOutputParser` / `JsonOutputParser`、`RunnableLambda`、临时记忆与文件持久化记忆
- 23–27：CSV/JSON/Text/PDF 文档加载器、`RecursiveCharacterTextSplitter` 文本切分、`InMemoryVectorStore` 向量检索
- 数据文件在 `resourse/`（`student.csv`、`data*.json`、`介绍.txt`、`填写说明.pdf` 等）

对话类脚本需要联网并消耗模型额度，使用 `DEEPSEEK_API_KEY`（DeepSeek）；向量化脚本使用 `ZHIPU_API_KEY`（智谱 AI）。23–26 的加载器脚本使用本地文件，可以离线运行。该目录为组件级练习，未包含完整的 RAG 问答链或 Agent 代码。

### coze

`AI Agent入门.py` 为概念笔记，记录 AI Agent 的定义和 Coze 平台的功能区域，没有实际代码。

### 练习项目

- 面向对象：`面向对象 上.py`（图书/书架）、`面向对象 学生管理系统 01.py`（内存版）、`面向对象 学生管理系统 02.py`（CSV 持久化版）
- 爬虫与可视化：`爬虫练习.py`、`检查.py`（requests + lxml + pandas/matplotlib，结果写入 `第五章/csv_data/`）
- PyTorch：`多特征线性回归.py`
- 其他：`实验.py`、`students.csv`

### 根目录其他文件

- `需要下载.py`：以注释形式记录 pip 安装命令
- `LICENSE`：MIT License
- `.venv/`：本地虚拟环境（未纳入版本控制）
- `.idea/`：PyCharm 项目配置（当前未提交）

## 环境与依赖

- Python 3.13（本地 `.venv` 版本为 3.13.14）
- 仓库没有提供 `requirements.txt`，依赖需要按需安装。根据代码中实际使用的库整理如下：

基础与数据分析：

```powershell
pip install jupyter pandas matplotlib
```

爬虫：

```powershell
pip install requests lxml
```

大模型与 AI 应用：

```powershell
pip install openai streamlit
pip install langchain langchain-community langchain-deepseek langchain-openai langchain-text-splitters pypdf jq
```

Web API：

```powershell
pip install fastapi uvicorn
```

深度学习：

```powershell
pip install torch numpy scikit-learn
```

语音克隆（仅 `第三章/AI应用/05 AI_partner 音频.py` 需要）：

```powershell
pip install librosa soundfile f5-tts
```

## 运行说明

1. 推荐在 PyCharm 中直接打开项目运行脚本；命令行运行时，中文或含空格的文件名需要用引号包起来：

```powershell
python "第一章/知识点/02 02if语句.py"
python "第四章/正则表达式.py"
```

2. API Key 通过环境变量配置，不要写进代码或提交到仓库：

```powershell
$env:DEEPSEEK_API_KEY = "你的 DeepSeek API Key"
$env:ZHIPU_API_KEY = "你的智谱 API Key"
```

3. 部分目录对工作目录有要求：

   - `第五章/` 的 Notebook 需要在 `第五章` 目录下启动 Jupyter，例如 `cd 第五章; jupyter notebook`
   - `第三章/AI应用/` 的 Streamlit 应用需要在该目录下运行，例如 `streamlit run "04 AI_partner.py"`
   - `langchain/` 的加载器脚本使用 `./resourse/...` 相对路径，需要在 `langchain` 目录下运行
   - `第四章/`、`练习项目/` 的部分脚本也使用相对路径，运行前注意当前目录

4. 网络相关示例：

   - `第六章/FastAPI基础.py` 启动后监听 `0.0.0.0:8000`，浏览器访问 `http://127.0.0.1:8000/`
   - 第七章的服务端/客户端示例需要先启动服务端，再启动客户端；代码中的 IP、端口和上传文件路径需要按本机情况修改

## 说明

- 这是一个个人学习仓库，代码按学习进度逐步补充，部分文件是纯注释笔记、空文件或未完成的草稿（例如 `算法详解/KMP算法.py`、`第六章/web AI汉字迷盒.py`），属于学习过程的一部分。
- 部分爬虫和网络示例使用了硬编码地址或依赖站点页面结构，运行前需要根据实际情况调整；爬虫请遵守目标站点的 robots 协议和使用条款。
- `*.py~` 是 PyCharm 自动生成的备份文件，可以忽略。
- 仓库中带有一些图片、视频和音频素材（第三章约 77 MB），克隆时仓库体积会稍大。

## License

MIT License，详见 [LICENSE](LICENSE)。
