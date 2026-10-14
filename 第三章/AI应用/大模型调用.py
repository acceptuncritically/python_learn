"""
# URL地址
curl https://api.deepseek.com/chat/completions \
  # 请求头 key：value
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${DEEPSEEK_API_KEY}" \
 # 请求体 json格式
  -d '{
    "model": "deepseek-flash",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Hello!"}
    ],
    "thinking": {"type": "enabled"},
    "reasoning_effort": "high",
    "stream": false
  }'

json 前端对象的表示方法 所有的key都要使用双引号引起来
对象用{} 键是字符串 值可以是其他类型
数字 字符串 布尔 true false
列表用[]
"""











# ==========================================
# 基于 cURL 命令提取的 HTTP 请求报文分析
# ==========================================
#
# 请求行(请求方式、资源路径、协议)
# POST /chat/completions HTTP/1.1
# (注：curl 默认根据 -d 参数推断为 POST 请求，Host 为 api.deepseek.com)
#
# 请求头(格式key：value)
# Content-Type: application/json
# Authorization: Bearer ${DEEPSEEK_API_KEY}
# Host: api.deepseek.com
# (注：curl 会自动补充 Host、Content-Length 等头部，图片中显式指定了前两个)
#
# 请求体(请求参数部分，GET方式没有，POST可以有)
# {
#     "model": "deepseek-flash",
#     "messages": [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Hello!"}
#     ],
#     "thinking": {"type": "enabled"},
#     "reasoning_effort": "high",
#     "stream": false
# }
#
# ==========================================
# cURL 命令参数与 HTTP 协议的对应关系：
# ==========================================
# 1. `curl https://api.deepseek.com/chat/completions`
#    -> 指定了协议(HTTPS)、Host(api.deepseek.com) 和 资源路径(/chat/completions)
# 2. `-H "Content-Type: application/json"`
#    -> 设置请求头 (Content-Type)，告诉服务端请求体的格式是 JSON
# 3. `-H "Authorization: Bearer ${DEEPSEEK_API_KEY}"`
#    -> 设置请求头 (Authorization)，用于身份验证 (Bearer Token)
# 4. `-d '...'`
#    -> 设置请求体 (-d 即 data)，并且自动将请求方式变成了 POST。
#       单引号内的 JSON 字符串就是真正的请求体内容。
#
# ==========================================
# 补充说明（关于请求体中的参数）：
# ==========================================
# - "model": "deepseek-flash" -> 指定调用的模型
# - "messages": [...]         -> 对话历史，包含 system（系统提示词）和 user（用户提问）
# - "thinking": {"type": "enabled"} -> 启用思考模式（类似于 DeepSeek-R1 的思维链）
# - "reasoning_effort": "high"      -> 设定推理强度为高
# - "stream": false                 -> 关闭流式输出（如果是 true，响应体会以 SSE 流式分块返回，对应上一图中的 Transfer-Encoding: chunked）