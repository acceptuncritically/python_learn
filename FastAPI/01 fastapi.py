from fastapi import FastAPI
import uvicorn  # 引入 uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/name")
async def read_name():
    return {"name": "ZhangSan"}

# 加上这段代码，当直接运行这个文件时，就会自动启动服务
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)