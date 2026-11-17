"""
使用依赖注入来共享通用逻辑，避免代码重复
依赖项：可重用的组件 负责提供某种功能和数据
注入：将依赖项提供给路由函数
多次复用 解耦 易于测试

与直接调用函数相比较
1 直接调用会使得之间用Query限制的内容无效，重新限制参数
    因为Query限制的内容是依赖项提供的，而不是路由函数直接使用的。
2 无法实现yield自动返回
"""

from fastapi import FastAPI,Query
from fastapi import Depends

app=FastAPI()

@app.get("/")
async def main(
        skip: int = Query(..., le=3, gt=1),
        limit: int = Query(..., le=5, gt=1)
):
    return {"skip": skip, "limit": limit}
@app.get("/items/")
async def name(comments=Depends(main)):
    return comments
@app.get("/user/")
async def name1():
    return "hello"
@app.get("/it/")
async def it(
    params: dict = Depends(main),          # 拿到 {"skip":..., "limit":...}
    keyword: str = Query("默认值"),          # 自己的新参数
):
    return {
        "skip": params["skip"],             # 复用 main 的结果
        "limit": params["limit"],
        "keyword": keyword,                 # 新增值
        "message": "这是新返回的值",
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8081)
