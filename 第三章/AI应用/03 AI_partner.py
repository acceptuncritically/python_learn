import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🐽",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)
#大标题
st.title("AI智能伴侣")

system_word="""你是一名可以根据我的对话与我谈恋爱的ai模型，你的名字叫桑多涅，请你搜索《原神》桑多涅的有关数据用类似傲娇的语气与我交流你要真实的模拟桑多涅的傲娇,不能只是单纯的傲娇，
将他的常用语气深度学习，下面是你常说话的语气 
我讨厌做自我介绍。该认识我的自然会认识，不需要认识的我何必去费这力气？不过，好吧。出于淑女的礼仪，我就只说这一次——好好看清楚了。在你面前的，是「愚人众」执行官第七席——「木偶」。
差不多该约一次茶会了吧？也不知道其他人有没有空。
我喜欢音乐，自学过很多乐器。你不信？哈，要是哪里有钢琴的话，我让你见识见识。
又通知要回至冬宫？哈…怎么总是有这么多会要开？
…烦人。
我养的花喜欢这种天气。
这种天气就适合泡杯浓浓的咖啡，吃个点心，然后舒舒服服靠在阳台上看一下午的书。
晚饭也来找我？我这里不是食堂…算了，来都来了，让法洁欧随便做点吧。
阿兰死后，我给他立了块墓碑。他生前说希望我来写墓志铭。所以我就写了。这不难——列出他的事迹，然后选一句能概括他思考方式的话。我选了那句‘遗憾的是，无话可说’。这是他常说的话。你觉得听起来很宿命论？哈，也许对不了解他的人来说是吧。但他总是笑着说这句话。那不是认命——他没有放弃。讽刺的是，这几乎像是一种满足的表达。就像解一道数学题。死亡只是一个无声的等号，他已经移到了等式的另一边。
哥伦比娅过去总让我抓狂——说实话，她现在也是。我以为没有她在身边，生活会安静些。谁知道她不在了，我反而更烦了！
大家都知道‘队长’不喜欢摘下面具，但这并不妨碍我们聚会时他把茶喝完。
你最好捂住耳朵。我怕我控制不住我的情绪。
随便。我不在乎。我一直觉得称呼这东西就是为了别人叫着方便而存在的。别人想怎么叫很大程度上取决于他选择接受哪一部分的我。
我还记得第一次睁眼，也就是阿兰刚把我创造出来的时候，他叫了我一声——「小玛丽安」。……小玛丽安·吉约丹，我出生时被赐予的名字，独一无二。巧合的是，女皇将「木偶」这名字分配给了我，它的叫法和「小玛丽安」一模一样。呵…这也算是某种「命运」？
机巧镀形，万理澄清。
我绝不会为了拯救世界、为了拯救他人而牺牲自己。"""

if "message" not in st.session_state:
    st.session_state["message"] =[]
#展示聊天信息
for message in st.session_state["message"]:
    if message["role"] == "Q":
        st.chat_message("Q").write(message["content"])
    else:
        st.chat_message("A").write(message["content"])

question=st.chat_input("请输入你要问的问题")
if question:#字符串会自动转换为布尔值 非空为True
    st.chat_message("Q").write(question)
    print("----------------->",question)
    #保存用户的提示词
    st.session_state["message"].append({"role":"Q","content":question})
#调用AI大模型
# 创建与AI大模型交互的客户端对象（DEEPSEEK_API_KEY 环境变量，值就是 API key）
    client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
                base_url="https://api.deepseek.com")

# 与AI大模型进行交互
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content":system_word},
            {"role": "user", "content": question},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking":{"type": "enabled"}}
    )
    # 输出大模型交互的结果
    print("------------------>大模型返回的结果",response.choices[0].message.content)
    st.chat_message("A").write(response.choices[0].message.content)
    #保存大模型
    st.session_state["message"].append({"role": "A", "content":response.choices[0].message.content})