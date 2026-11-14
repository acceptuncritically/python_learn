"""
在http协议中 一个完整的请求由 请求头请求行和请求体三部分组成
请求行：包含 方法 URL 协议版本
请求头：元数据信息
请求体：实际要发送的内容
"""
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
#注册 用户名和密码
class User(BaseModel):
    # 将需要的属性写到实例中
    username: str
    password: str
# 结果并不会直接拼接到URL中，会在-d请求体中
@app.post("/register")
async def register(user: User):
    return {"username": user.username, "password": user.password}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
