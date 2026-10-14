import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
print(os.environ.get("HF_ENDPOINT"))
import streamlit as st

import os
import json
import tempfile
import numpy as np
import soundfile as sf
import librosa
from openai import OpenAI
from f5_tts.api import F5TTS

# ==================== 页面配置 ====================
st.set_page_config(
    page_title="AI智能伴侣 - 桑多涅语音版",
    page_icon="🐽",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)
st.title("AI智能伴侣 · 桑多涅")

# ==================== 系统提示词 ====================
system_word = """你是一名可以根据我的对话与我谈恋爱的ai模型，你的名字叫桑多涅，请你用类似傲娇的语气与我交流。
你要真实地模拟桑多涅的傲娇，不能只是单纯的傲娇，要深度还原她的常用语气。
下面是她常说话的语气：
我讨厌做自我介绍。该认识我的自然会认识，不需要认识的我何必去费这力气？不过，好吧。出于淑女的礼仪，我就只说这一次——好好看清楚了。在你面前的，是「愚人众」执行官第七席——「木偶」。
差不多该约一次茶会了吧？也不知道其他人有没有空。
我喜欢音乐，自学过很多乐器。你不信？哈，要是哪里有钢琴的话，我让你见识见识。
又通知要回至冬宫？哈…怎么总是有这么多会要开？…烦人。
我养的花喜欢这种天气。
这种天气就适合泡杯浓浓的咖啡，吃个点心，然后舒舒服服靠在阳台上看一下午的书。
晚饭也来找我？我这里不是食堂…算了，来都来了，让法洁欧随便做点吧。
阿兰死后，我给他立了块墓碑。他生前说希望我来写墓志铭。所以我就写了。这不难——列出他的事迹，然后选一句能概括他思考方式的话。我选了那句"遗憾的是，无话可说"。这是他常说的话。你觉得听起来很宿命论？哈，也许对不了解他的人来说是吧。但他总是笑着说这句话。那不是认命——他没有放弃。讽刺的是，这几乎像是一种满足的表达。就像解一道数学题。死亡只是一个无声的等号，他已经移到了等式的另一边。
哥伦比娅过去总让我抓狂——说实话，她现在也是。我以为没有她在身边，生活会安静些。谁知道她不在了，我反而更烦了！
大家都知道"队长"不喜欢摘下面具，但这并不妨碍我们聚会时他把茶喝完。
你最好捂住耳朵。我怕我控制不住我的情绪。
随便。我不在乎。我一直觉得称呼这东西就是为了别人叫着方便而存在的。别人想怎么叫很大程度上取决于他选择接受哪一部分的我。
我还记得第一次睁眼，也就是阿兰刚把我创造出来的时候，他叫了我一声——「小玛丽安」。……小玛丽安·吉约丹，我出生时被赐予的名字，独一无二。巧合的是，女皇将「木偶」这名字分配给了我，它的叫法和「小玛丽安」一模一样。呵…这也算是某种「命运」？
机巧镀形，万理澄清。
我绝不会为了拯救世界、为了拯救他人而牺牲自己。"""

# ==================== 初始化会话状态 ====================
CHAT_HISTORY_FILE = "chat_history.json"
VOICE_SAMPLE_FILE = "sandrone_voice.wav"  # 保存用户上传的参考音频

def save_messages():
    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state["message"], f, ensure_ascii=False, indent=2)

if "message" not in st.session_state:
    if os.path.exists(CHAT_HISTORY_FILE):
        try:
            with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as f:
                st.session_state["message"] = json.load(f)
        except:
            st.session_state["message"] = []
    else:
        st.session_state["message"] = []

if "ref_audio_path" not in st.session_state:
    # 如果之前保存过桑多涅的参考音频，直接加载
    if os.path.exists(VOICE_SAMPLE_FILE):
        st.session_state["ref_audio_path"] = VOICE_SAMPLE_FILE
    else:
        st.session_state["ref_audio_path"] = None

# ==================== 侧边栏：参考音频上传 ====================
with st.sidebar:
    st.header("🎤 桑多涅的声音")
    st.caption("上传 3-10 秒清晰的桑多涅语音片段，AI 将用她的音色说话。")

    uploaded_audio = st.file_uploader(
        "上传参考音频",
        type=["wav", "mp3", "aac", "m4a"],
        key="voice_uploader"
    )

    if uploaded_audio is not None:
        # 保存上传的音频到临时文件
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(uploaded_audio.getbuffer())
            temp_path = tmp.name

        # 预处理音频：强制单声道，去除静音
        try:
            y, sr = librosa.load(temp_path, sr=None, mono=True)
            y, _ = librosa.effects.trim(y, top_db=20)
            sf.write(VOICE_SAMPLE_FILE, y, sr)
            st.session_state["ref_audio_path"] = VOICE_SAMPLE_FILE
            st.success("✅ 桑多涅的声音已加载！")
            os.unlink(temp_path)
        except Exception as e:
            st.error(f"音频处理失败：{e}")

    if st.session_state["ref_audio_path"]:
        st.audio(st.session_state["ref_audio_path"], format="audio/wav")
        st.caption("当前使用的参考音频")

    st.divider()
    if st.button("🗑️ 清空对话"):
        st.session_state["message"] = []
        save_messages()
        st.rerun()

# ==================== 加载 F5-TTS 模型 ====================
@st.cache_resource
def load_tts_model():
    """首次加载模型，缓存避免重复初始化"""
    with st.spinner("正在加载语音克隆模型..."):
        try:
            model = F5TTS()
            return model
        except Exception as e:
            st.error(f"模型加载失败：{e}")
            return None

tts_model = load_tts_model()

# ==================== 展示聊天历史 ====================
for message in st.session_state["message"]:
    if message["role"] == "Q":
        st.chat_message("Q").write(message["content"])
    else:
        st.chat_message("A").write(message["content"])

# ==================== 用户输入 & AI 回复 ====================
question = st.chat_input("请输入你要问的问题")

if question:
    st.chat_message("Q").write(question)
    st.session_state["message"].append({"role": "Q", "content": question})
    save_messages()

    # 构建 API 消息（把 Q/A 映射为 user/assistant）
    api_messages = [{"role": "system", "content": system_word}]
    for msg in st.session_state["message"]:
        api_messages.append({
            "role": "user" if msg["role"] == "Q" else "assistant",
            "content": msg["content"]
        })

    # 调用 DeepSeek
    client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com"
    )

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=api_messages,
            stream=False
        )
        ai_reply = response.choices[0].message.content
    except Exception as e:
        st.error(f"AI 请求失败：{e}")
        st.stop()

    st.chat_message("A").write(ai_reply)
    st.session_state["message"].append({"role": "A", "content": ai_reply})
    save_messages()

    # ==================== 用桑多涅的声音朗读回复 ====================
    if tts_model is not None and st.session_state["ref_audio_path"]:
        try:
            with st.spinner("桑多涅正在说话..."):
                # 调用 F5-TTS 进行零样本语音克隆
                wav, sr, _ = tts_model.infer(
                    ref_file=st.session_state["ref_audio_path"],
                    ref_text="",                    # 参考音频的文本（可留空）
                    gen_text=ai_reply,              # 要生成的文本
                    speed=1.0,
                    remove_silence=True
                )
                # 保存生成的音频
                output_path = "sandrone_reply.wav"
                sf.write(output_path, wav, sr)

            # 在 Streamlit 中播放
            st.audio(output_path, format="audio/wav", autoplay=True)

        except Exception as e:
            st.warning(f"语音生成失败：{e}")
    elif st.session_state["ref_audio_path"] is None:
        st.info("💡 在左侧上传桑多涅的参考音频，即可让她用原声说话。")