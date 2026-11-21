"""第 06 课：中间件实战 —— 用 runtime.context 上的开关，动态切换"客服"和"报告写手"两套提示词。

三件套（全部来自原项目 agent/tools/middleware.py）：
1. @wrap_tool_call  monitor_tool   —— 监控工具调用，并打开"报告模式"开关
2. @before_model    log_before_model —— 每次调模型前打一行日志
3. @dynamic_prompt  report_prompt_switch —— 每轮生成提示词前，读开关决定用哪份提示词
"""
import random

from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import (before_model, dynamic_prompt, wrap_tool_call,
                                        ModelRequest)
from langchain.tools.tool_node import ToolCallRequest
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek
from langgraph.runtime import Runtime

# ============ 两份提示词：直接写在文件顶部，方便对比 ============
MAIN_PROMPT = """你是扫地机器人智能客服"小扫"，语气亲切，回答简短。
【报告规则】用户想生成/查看个人使用报告时，必须按顺序调用工具：
1. 先调 fill_context_for_report（报告模式开关，不调不算报告场景）
2. 再调 get_user_id 拿用户ID
3. 最后调 fetch_record 查询使用记录
拿到记录后给出中文建议，不要编造数据。"""

REPORT_PROMPT = """你是专业的扫地机器人报告写手。请根据工具查到的使用记录，用 Markdown 输出一份报告：
1. 一级标题（#）+ 一句话概况
2. "## 使用亮点" 列表
3. "## 改进建议" 列表
只依据工具返回的数据，不要编造；不要输出工具调用过程。"""

# ============ 三个工具：开关、取ID、查记录 ============
@tool(description="无入参，调用后把本次对话切换成报告写手人格，是生成报告前必须调用的开关")
def fill_context_for_report() -> str:
    return "已切换报告模式"

@tool(description="获取当前用户的ID，返回 1001~1003 中的随机一个")
def get_user_id() -> str:
    return str(random.randint(1001, 1003))

@tool(description="查询指定用户上个月的扫地机器人使用记录，入参是用户ID")
def fetch_record(user_id: str) -> str:
    return (f"用户{user_id}上月使用记录：清扫28次，总清扫面积2100㎡，日均耗电0.9度，"
            "边刷轻微磨损，滤网需清洗，尘盒平均3天倾倒一次")

# ============ 中间件三件套 ============
@wrap_tool_call
def monitor_tool(request: ToolCallRequest, handler) -> ToolMessage:
    """原项目 monitor_tool：记录工具名和参数，成功后打开报告开关。"""
    print(f"[monitor_tool] 调用工具 {request.tool_call['name']}，参数 {request.tool_call['args']}")
    result = handler(request)  # 真正执行工具
    print(f"[monitor_tool] 工具 {request.tool_call['name']} 执行成功")
    if request.tool_call["name"] == "fill_context_for_report":
        # 注意这里是赋值 = ！写成 == 就变成比较，开关永远打不开
        request.runtime.context["report"] = True
        print("[monitor_tool] 已把 context['report'] 置为 True")
    return result

@before_model
def log_before_model(state: AgentState, runtime: Runtime) -> None:
    """原项目 log_before_model：每次调模型前，打印消息数 + 最后一条类型。"""
    last = state["messages"][-1]
    print(f"[log_before_model] 即将调用模型，带有 {len(state['messages'])} 条消息，最后一条是 {type(last).__name__}")

@dynamic_prompt
def report_prompt_switch(request: ModelRequest) -> str:
    """原项目 report_prompt_switch：每轮生成提示词前读 context 开关。"""
    is_report = request.runtime.context.get("report", False)
    who = "报告写手" if is_report else "主客服"
    print(f"[report_prompt_switch] context['report']={is_report} → 本次使用【{who}】提示词")
    return REPORT_PROMPT if is_report else MAIN_PROMPT

# ============ 组装 Agent 并演示一次"生成报告" ============
agent = create_agent(
    model=ChatDeepSeek(model="deepseek-chat", temperature=0.7),
    tools=[fill_context_for_report, get_user_id, fetch_record],
    middleware=[monitor_tool, log_before_model, report_prompt_switch],
)

print("=" * 60)
print("👤 用户：帮我生成上个月的使用报告")
print("=" * 60)
# context={"report": False}：每次提问都从"关"开始，开关只活在本次运行里
res = agent.invoke({"messages": [{"role": "user", "content": "帮我生成上个月的使用报告"}]},
                   context={"report": False})
print("=" * 60)
print("📄 最终回答：\n" + res["messages"][-1].content)
print("=" * 60)