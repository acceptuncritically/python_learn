from fastapi import FastAPI
import uvicorn  # 引入 uvicorn
from typing import Annotated
from fastapi import Query, Path

app = FastAPI()
"""
想要定位某一个具体的资源（比如查第 1 号用户），用 Path：/users/1
想要过滤、搜索、分页（比如按名字搜用户，或者翻第 2 页），用 Query：/users?name=张三&page=2
"""
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")# 注意路由里有 /{item_id}
# 在/items/后直接接上，不可以设置默认值，必须填写内容
async def read_item(
    # 必须使用 Annotated 结合 Path 来做校验
    item_id: Annotated[int, Path(title="商品ID", gt=0, lt=1000)]
):
    return {"item_id": item_id, "message": "这是一个路径参数"}
@app.get("/name")
# 在URL后的问号后通过key value的方式填写，可以设置默认值，可选择是否填写
async def read_name(name:Annotated[str|None,Query(min_length=1,max_length=10)]=None,age:Annotated[int|None,Query(gt=0,lt=100)] = None):
    return {"name": f"name is {name}, age is {age}"}

# 加上这段代码，当直接运行这个文件时，就会自动启动服务
if __name__ == "__main__":
    # reload = True不能用app实例实现
    uvicorn.run(app, host="127.0.0.1", port=8000, )
