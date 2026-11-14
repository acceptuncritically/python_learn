# 为了解决调用大模型时响应速度过慢的问题，可以使用异步IO（asyncio）来实现。
# 保证多个事情之间同时进行方式 由于等待导致时间消耗过长
import asyncio
# 在其中同时执行的任务只能有一个，需要主动告诉eventloop开始
async def print_content():
    print("开始执行任务2")
# 这为一个coroutine function
async def main():
    print("开始执行任务1")
    await asyncio.sleep(2)
    print("任务1执行完成")
    # 会返回一个coroutine 对象并不会执行main函数里的代码

async def after_main():
    # 有两种方法将coroutine 转换为task：creat_task 和gather
    task=asyncio.create_task(print_content())
    await task
    await asyncio.gather(
        print_content(),
        print_content(),
    )
asyncio.run(after_main())
