#对于客户端没有找到的情况，
#使用fastapi.HTTPException,中断正常处理流程，返回标准错误响应
from fastapi import FastAPI,HTTPException


app=FastAPI()
@app.get("/")
async def root():
    return "hello world"
@app.get("/{id}")
async def get_id(id:int):
    my_list=[i for i in range(1,11)]
    if id not in my_list:
        raise HTTPException(status_code=404,detail="并没有找到此id")
    return {"id":id}
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8080)