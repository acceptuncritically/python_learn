"""
中间件可以解决 日志记录 身份认证 跨域处理 响应头处理 和性能监控等问题
作用：为每个请求添加统一的处理逻辑，如身份认证、日志记录等
执行顺序：类似于栈采用包洋葱的顺序输出
"""
from fastapi import FastAPI,Request,Response

app=FastAPI()

@app.get("/")
async def main():
    return "hello world"

@app.middleware("http")
async def middleware1(request,call_next):
    print("中间件1开始处理--start")
    response = await call_next(request)
    print("中间件1结束处理--end")
    return response
@app.middleware("http")
async def middleware2(request,call_next):
    print("中间件2开始处理--start")
    response = await call_next(request)
    print("中间件2结束处理--end")
    return response
"""
request是一个object对象 获得用户输入的值
call_next本质是一个异步函数 调用下一个中间件或目标函数
        将request传给下一个中间件或目标函数
await 表示在走到这一步时，会等待call_next(request)的返回结果
        但不代表程序堵塞，python有Event loop机制会自动运行下一个内容
在普通路由里要加上request:Request表示不是一个普通的参数
"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8081)
