"""
默认FastAPI 会将路径函数返回的python对象
经由jsonable_encoder 转换为json格式JSON格式 并包装为JSONResponse返回
如果想要返回非json格式数据 可以使用可以通过改变相应类型返回对应数据
"""
"""
如果需要返回非 JSON 数据（如 HTML、文件流），FastAPI 提供了丰富的响应类型来返回不同数据

--------------------------------------------------------------------------------------------
| 响应类型           | 用途                   | 示例                                 |
--------------------------------------------------------------------------------------------
| JSONResponse       | 默认响应，返回JSON数据 | return {"key": "value"}              |
| HTMLResponse       | 返回HTML内容           | return HTMLResponse(html_content)    |
| PlainTextResponse  | 返回纯文本             | return PlainTextResponse("text")     |
| FileResponse       | 返回文件下载           | return FileResponse(path)            |
| StreamingResponse  | 流式响应               | 生成器函数返回数据                   |
| RedirectResponse   | 重定向                 | return RedirectResponse(url)         |
--------------------------------------------------------------------------------------------
"""
