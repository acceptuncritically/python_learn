from operator import index

import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': "https://ys.mihoyo.com/?utm_source=backup307&from_channel=backup307#/",
        'Report a bug': "https://ys.mihoyo.com/?utm_source=backup307&from_channel=backup307#/",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



#大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

#段落文字
st.write("桑多涅并非人类，她的本名是小玛丽安·吉约丹。她是由枫丹的天才“奇械公”阿兰·吉约丹，")
st.write("为了纪念自己早逝的妹妹玛丽安，在六十五岁生日时亲手创造的奇械人偶。")
st.write("阿兰将她视为家人，希望她能“随心所欲地做任何事”，拥有属于自己的人生。")
st.write("桑多涅的性格非常复杂。她对自己有着极强的自信，言语间充满居高临下的傲慢与反讽，")
st.write("坚信未知无非是可被演算驱散的迷雾。然而，这层冰冷的外壳下，隐藏着典型的“傲娇”本质")
# 图片
# st.image("./resourses/桑多涅.jpg")
# st.image("./resourses/桑多涅.jpg")

#视频
st.video("./resourses/桑多涅视频.m4s")
#音频
st.audio("./resourses/桑多涅音频.m4s")
#logo
st.logo("./resourses/桑多涅.jpg")#出现在左上角
#表格
student_data = {
    "姓名": ["王林", "李慕婉", "贝罗", "莫厉海", "石萧"],
    "学号": ["20260001", "20260002", "20260003", "20260004", "20260005"],
    "语文": [98, 90, 59, 29, 80],
    "数学": [88, 78, 65, 70, 39],
    "英语": [99, 89, 87, 59, 62],
    "总分": [285, 257, 211, 158, 181]
}
st.table(student_data)
#输入
name=st.text_input("请输入你的名字")
#有type参数 默认是文本 password 是密码形式
st.write(f"您的名字是:{name}")
password=st.text_input("请输入你的名字",type="password")
#有type参数 默认是文本 password 是密码形式
st.write(f"您的名字是:{password}")

#单选按钮
gender=st.radio("请输入您的性别",["男","女","未知"],index=2)
st.write(f"您的性别是：{gender}")