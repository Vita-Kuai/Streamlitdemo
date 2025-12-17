# Streamlit14.py
import streamlit as st  # 匯入 Streamlit 並用 st 代表它
import pandas as pd

df = pd.DataFrame({"1 號店": [100, 230], "2 號店": [120, 220], "3 號店": [190, 320]})

# 傳入多個參數
st.write("2 * 3=", 6)
st.write("下面是門店資料 ", df, "上面是門店資料")
