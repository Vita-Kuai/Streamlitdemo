# Streamlit16.py
import streamlit as st
import pandas as pd

st.title("Hello Streamlit 👋")

name = st.text_input("請輸入你的名字")
age = st.slider("請輸入年齡", 0, 100, 25)

if st.button("送出"):
    st.write(f"Hello {name}, 你今年 {age} 歲！")

# 顯示表格
data = pd.DataFrame({
    "城市": ["台北", "台中", "高雄"],
    "人口(萬)": [270, 280, 290]
})
st.dataframe(data)
