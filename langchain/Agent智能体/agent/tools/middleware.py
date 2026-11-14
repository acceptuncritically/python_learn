from langchain.agents import AgentState
from langchain.agents.middleware import wrap_tool_call, before_model, dynamic_prompt, ModelRequest
from langchain.tools.tool_node import ToolCallRequest
from typing import Callable
from main.prompt_loader import load_system_prompts,load_report_prompts
from langgraph.runtime import Runtime
from langgraph.types import Command
from langchain_core.messages import ToolMessage

from main.log_handler import logger

@wrap_tool_call
def monitor_tool(
        #请求的数据封装
        request:ToolCallRequest,
        #执行的函数本身
        handler:Callable[[ToolCallRequest], ToolMessage|Command]
)->ToolMessage|Command:             #工具执行的监控
    logger.info(f"Tool call执行工具: {request.tool_call['name']}")
    logger.info(f"Tool call传入参数: {request.tool_call['args']}")
    try:
        result=handler(request)
        logger.info(f"Tool call工具调用成功:{request.tool_call['name']}")
        if request.tool_call['name']=="fill_context_for_report":
            request.runtime.context['report'] == True
        return result
    except Exception as e:
        logger.error(f"Tool call {request.tool_call['name']}执行工具出错: {e}")
        raise e
@before_model
def log_before_model(
        state:AgentState,       #整个智能体中的状态信息
        runtime:Runtime         #记录了整个执行过程中的上下文信息
):         #在模型执行前输出日志
    logger.info(f"[log_before_model]即将调用模型，带有{len(state['messages'])}条信息")
    logger.debug(f"[log_before_model]{type(state['messages'][-1]).__name__}|{state['messages'][-1].content}")
@dynamic_prompt     #每一次生成提示词前，调用此函数
def report_prompt_switch(request:ModelRequest) :     #动态提示词切换
    is_report = request.runtime.context.get('report', False)
    if is_report:
        return load_report_prompts()
    else:
        return load_system_prompts()
