from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
#先设置类确定数据类型
class News(BaseModel):
    title:str
    id:int
    content:str
@app.get("/news")
async def main():
    return "hello world"
@app.get("/news/{id}",response_model=News)
async def news(id:int):
    # 路径中声明了{id}，那么对应的处理函数news中必须有一个同名参数id来接收它。
    return {
        "title":"hello world",
        "id":id,
        "content":"this is a test"
    }
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
