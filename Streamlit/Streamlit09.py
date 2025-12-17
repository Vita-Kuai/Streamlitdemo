# Streamlit09.py
import pandas as pd  # 匯入 Pandas 並用 pd 代替
import streamlit as st  # 匯入 Streamlit 並用 st 代表它

# 定義資料 ,以便建立資料框
data = {
    "1 號門店 ": [568, 868, 670, 884, 144],
    "2 號門店 ": [820, 884, 768, 524, 709],
    "3 號門店 ": [577, 532, 996, 929, 694],
}

# 定義資料框所用的索引
index = pd.Series(["01 月", "02月", "03月", "04月", "05月"], name="月份")

# 根據上面建立的 data 和 index 建立資料框
df = pd.DataFrame(data, index=index)
st.subheader("預設顯示")
st.dataframe(df)

st.subheader("設定寬度和高度")
st.dataframe(df, width=400, height=150)

st.subheader("設定為父容器的寬度 ")
st.dataframe(df, use_container_width=True)
