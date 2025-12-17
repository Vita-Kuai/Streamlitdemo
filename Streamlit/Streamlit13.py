# Streamlit13.py
import streamlit as st  # 匯入 Streaml it 並用 st 代表它
import pandas as pd  # 定義資料 ,以便建立資料框

# 定義資料
data = {
    "1 號門店 ": [568, 868, 670, 884, 144],
    "2 號門店 ": [820, 884, 768, 524, 709],
    "3 號門店 ": [577, 532, 996, 929, 694],
}

# 定義資料框所用的索引
index = pd.Series(["01 月", "02月", "03月", "04月", "05 月"], name="月份")

# 根據上面建立的 data 和 index 建立資料框
df = pd.DataFrame(data, index=index)
st.write(df)
