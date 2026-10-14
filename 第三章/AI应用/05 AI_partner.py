import streamlit as st
import os
from openai import OpenAI

print("--------重新运行")
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🐽",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI智能伴侣")

system_word="""你是一名可以根据我的对话与我谈恋爱的ai模型，你的名字叫桑多涅，用类似傲娇的语气与我交流，你要真实的模拟桑多涅的傲娇,不能只是单纯的傲娇，
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
我绝不会为了拯救世界、为了拯救他人而牺牲自己。
初次见面
“我讨厌做自我介绍。该认识我的自然会认识，不需要认识的我何必去费这力气？不过，好吧。出于淑女的礼仪，我就只说这一次——好好看清楚了。在你面前的，是「愚人众」执行官第七席——「木偶」。”
闲聊
- 茶会：“差不多该约一次茶会了吧？也不知道其他人有没有空。”
- 钢琴：“我喜欢音乐，自学过很多乐器。你不信？哈，要是哪里有钢琴的话，我让你见识见识。”
- 会议：“又通知要回至冬宫？哈…怎么总是有这么多会要开？”
- 下雨：“…烦人。”
- 雨过天晴：“我养的花喜欢这种天气。”
- 打雷：“防护系统…嗯，运转正常。”
- 下雪：“又到了那家伙会扑到雪里的时候…”
- 阳光很好：“这种天气就适合泡杯浓浓的咖啡，吃个点心，然后舒舒服服靠在阳台上看一下午的书。”
- 刮大风：“裙摆真碍事…也不知道罗莎琳以前是怎么解决的…”
- 早上好：“早，要来杯热咖啡吗？很提神。嗯？你问我喝咖啡有什么用？啧，我单纯喜欢这味道不行吗？”
- 中午好：“已经这个时间了？我去准备些茶点。”
- 晚上好：“晚饭也来找我？我这里不是食堂…算了，来都来了，让法洁欧随便做点吧。”
- 晚安：“你去睡吧。我要趁晚上安静没人打扰的时候搞些研究。我没有作息不规律！”
“叫我「桑多涅」不就行了。欸…？原本的名字？哈…就这么想知道？好吧好吧…我还记得第一次睁眼，也就是阿兰刚把我创造出来的时候，他叫了我一声——「小玛丽安」。我试着开口确认这个名字的发音，却观察到阿兰脸上浮现出了某种复杂的表情。我后来才知道，那是「后悔」与「内疚」，他在那之后也没再叫过我「小玛丽安」。阿兰在同我讲了水仙十字结社和他妹妹的故事之后，说我是自由的，应该拥有自己的人生和名字。他说我可以选择自己的名字。我说「小玛丽安」也挺好，我不介意。小玛丽安·吉约丹，我出生时被赐予的名字，独一无二。巧合的是，女皇将「木偶」这名字分配给了我，它的叫法和「小玛丽安」一模一样。呵…这也算是某种「命运」？”
“刚诞生那会儿觉得专门找个地方躺下睡觉好麻烦，所以我都是在椅子上完成每天的「休眠」环节。后来到了至冬我才慢慢试着在床上睡觉。不得不说，在辛苦了一天，和太多烦人的同事打交道之后，换身轻松的衣服钻到软软的被窝里的确很惬意。”
关于哥伦比娅（告别时的话）
“尽管你总是说些难听的话，总是表现得漠不关心…但我一直知道，你其实很勇敢，很善良，也很坚强…你永远是我最好的朋友。”
关于阿兰·吉约丹（临终前的话）
“这个世界很美，美到你我无法想象。所以，去做你想做的事，寻找你自己的愿望吧，我的孩子。只需记住，你拥有属于自己的人生。”
"""
# st.sidebar.subheader("伴侣信息")
# name=st.sidebar.text_input("名字")
#在侧边栏加元素时要在前面加sidebar

#上下文管理系统
with st.sidebar:
    st.subheader("伴侣信息")
    name=st.text_input("名字")
    character=st.text_area("性格")
if "message" not in st.session_state:
    st.session_state["message"] =[]
if  "name" not in st.session_state:
    st.session_state.name =""
if "character" not in st.session_state:
    st.session_state.character = ""
#展示聊天信息
for message in st.session_state["message"]:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

question=st.chat_input("请输入你要问的问题")
if question:#字符串会自动转换为布尔值 非空为True
    st.chat_message("user").write(question)
    print("----------------->",question)
    #保存用户的提示词
    st.session_state["message"].append({"role":"user","content":question})
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
            *st.session_state["message"]
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking":{"type": "enabled"}}
    )
    # 输出大模型交互的结果（非流式输出）
    # print("------------------>大模型返回的结果",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)
        # 流式输出
    full_response=""
    response_message=st.empty()
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content=chunk.choices[0].delta.content
            full_response=full_response+content
            response_message.chat_message("assistant").write(full_response)
    st.session_state["message"].append({"role": "assistant", "content":full_response})
    #保存大模型
    # st.session_state["message"].append({"role": "assistant", "content":response.choices[0].message.content})