HTTP协议 超文本传输协议 规定客户端与服务端之间的格式
1.基于文本的协议：请求和相应部分的协议内容为文本格式，底层通过TCP此协议传输，稳定性强
2.基于请求响应模型 一次请求一次响应，必须客户端请求 服务端才会响应
3.无状态：服务端不会记忆与客户端的历史交互信息 每一次请求响应都是独立的

==========================================
HTTP 请求格式分析
==========================================

请求行(请求方式、资源路径、协议)
POST /api/courses HTTP/1.1

请求头(格式key：value)
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Content-Length: 139
Content-Type: application/json
Host: localhost:90
Origin: http://localhost:90
Referer: http://localhost:90/resource/course
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/143.0.0.0

请求体(请求参数部分，GET方式没有，POST可以有)
{"phone":"18808088080","channel":1, "name":"虎跑","gender":1,"age":"32"}

请求方式：
· GET：请求参数在请求行中，没有请求体。如：/api/courses?name=Python&status=1 。GET请求请求参数大小在浏览器中是有限制的。
· POST：请求参数在请求体中，POST请求大小是没有限制的。

-------------------------------------------------------
==========================================
HTTP协议 - 响应数据格式
==========================================

响应行(协议、状态码)
HTTP/1.1 200

响应头(格式key：value)
Server: nginx/1.24.0
Date: Tue, 16 Dec 2025 12:38:08 GMT
Content-Type: application/json
Transfer-Encoding: chunked
Connection: keep-alive

响应体(存放服务端响应的数据)
{code: 1, msg: "success", data: null}

------------------------------------------
常见HTTP响应状态码说明：
200: 客户端请求成功
400: 请求参数错误
404: 请求资源不存在，url输入有误，或者网站资源被删除了
500: 服务器发生了不可预期的错误

1xx（信息性状态码）：
如 100 Continue、101 Switching Protocols。这些响应只是中间状态，不包含响应体。
204 No Content：
表示请求成功，但服务器没有返回任何内容（比如删除资源成功，通常不需要返回数据）。
304 Not Modified
：表示资源未修改，客户端可以直接使用本地缓存。这种情况下服务器也不会返回响应体。