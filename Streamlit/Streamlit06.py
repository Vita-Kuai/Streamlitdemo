# Streamlit06.py
import streamlit as st

st.header("這是一個章節展示元素 ")
st.subheader("這是一個子章節展示元素 ")
st.text("這是普通文字展示元素")

python_code = """def hello():
    print ("你好 ,Streamlit ! ")
"""
#  unsafe_allow_html : 在預設情況下 ,在 body 字串中找到的任何 HTML 標記都將被跳脫 ,因此被視為純文字 。可以透過將此參數設定為 True 來關開此行為。該參數會存在一些安全隱憂 ,官方建議將此參數設定為 False。
# 預設說明文件
st.caption("程式區塊 1: Python 程式")
st.caption("<i> 程式區塊1: Python 程式 </i>", unsafe_allow_html=True)

# 叠中對齊的說明文字樣式
st.caption("<center> 程式區塊 1: Python 程式 </center>", unsafe_allow_html=True)
st.code(python_code)
