# Streamlit01.py
# 匯入 Streaml it 並用 st 代表它
import streamlit as st

# 第 1 個普通文字展示元素，無工具提示
st.text("這是一個普通文字展示元素。")

# 第 2 個普通文字展示元素，有工具提示
st.text("這也是一個普通文字展示元素，帶有工具提示", help="這是工具提示")

# 第 3 個普通文字展示元素，展示一些跳脱字元
st.text("""親愛的讀者，\n你們好!\t歡迎學習 Streamlit""")
