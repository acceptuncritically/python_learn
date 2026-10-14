import uvicorn
from fastapi import FastAPI

# 两种运行的方式
# fastapi dev "xxxx.py"
# uvicorn xxxx:app --reload

#创建fastapi的实例
app = FastAPI()

#定义API接口-- 该函数的返回值表示APi接口
@app.get("/")
def root():
    return {"message": "Hello World"}

#定义API接口
@app.get("/users")
def get_users():
    return [
        {"name": "John", "age": 25},
        {"name": "Michael", "age": 26},
        {"name": "Ben", "age": 28},
    ]
# uvicorn python 中轻量的服务器
if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)