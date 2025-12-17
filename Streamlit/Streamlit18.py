# Streamlit18.py
import streamlit as st

st.title("BMI 計算器 🧮")

# Sidebar 輸入
st.sidebar.header("輸入資料")
height = st.sidebar.number_input("身高 (cm)", 150, 200, 170)
weight = st.sidebar.number_input("體重 (kg)", 40, 120, 65)
if st.sidebar.button("開始計算"):
    # 計算
    bmi = weight / ((height / 100) ** 2)

    st.write(f"你的 BMI 值為：**{bmi:.2f}**")

    if bmi < 18.5:
        st.warning("過輕")
    elif 18.5 <= bmi < 24:
        st.success("正常")
    else:
        st.error("過重")

    st.write("請根據你的 BMI 值，調整你的飲食與運動習慣！")
    st.balloons()  # 氣球效果
    st.snow()  # 冰雪效果
    st.toast("計算完成！")  # 通知效果

import streamlit as st
import time

