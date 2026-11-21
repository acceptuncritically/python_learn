"""
使用create_async_engine创建异步引擎
orm是一种编程技术，在面向对象编程和关系类数据库之间建立映射，
无需编写SQL语句，通过操作对象的方式来与数据库进行交互
"""
from sqlalchemy import func, DateTime, String, Float
from sqlalchemy.ext.asyncio import create_async_engine
from fastapi import FastAPI
from sqlalchemy.orm import DeclarativeBase, Mapped,mapped_column
from datetime import datetime

#创建异步引擎
ASYNC_DATABASE_URL='mysql+aiomysql://root:331721@localhost:3306/FastAPI_first?charset=utf8'
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True, #输出sql日志
    pool_size=10,   #设置连接池活跃的连接数
    max_overflow=20,    #允许额外的连接数
)

#定义模型类 :基类＋表
class Base(DeclarativeBase):
    """
    定义模型类的基类
    create_time 为创建时间，默认值为当前时间，不可更新
        DateTime是类型，
        insert_default= （数据库中的默认值），default= （Python中的默认值）
        func它是 SQLAlchemy 提供的一个工具，用来调用数据库里的原生 SQL 函数
        func.time 获得当前时间
    update_time 以当前时间为默认值，当改变数据库的内容时自动更新
        onupdate=datetime.now  当更新数据时，自动更新时间为当前时间
    """
    create_time:Mapped[datetime]=mapped_column(DateTime, insert_default=func.now(), default=datetime.now)
    update_time:Mapped[datetime]=mapped_column(DateTime, insert_default=func.now(), default=datetime.now, onupdate=datetime.now)


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True, comment="书籍id")
    bookname: Mapped[str] = mapped_column(String(255), comment="书名")
    author: Mapped[str] = mapped_column(String(255), comment="作者")
    price: Mapped[float] = mapped_column(Float, comment="价格")

#建表：定义函数建表->FastAPI启动时调用建表的函数
async def create_table():
    #获取异步引擎，创建事务->建表
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)#Base 模型类的元数据加载


from contextlib import asynccontextmanager

#由于原本的 on_event已经弃用
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup code
    await create_table()
    yield
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return "hello world"
