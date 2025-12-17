# Streamlit19.py
import streamlit as st
import pandas as pd
import numpy as np

st.title("隨機數據折線圖 📈")

n = st.slider("請選擇資料筆數", 10, 100, 20) # 10~100,預設20

data = pd.DataFrame({
    "x": range(n),
    "y": np.random.randint(1, 100, n)
})
# x 軸為 n筆資料, y 軸為 隨機資料數值

st.line_chart(data.set_index("x"))
