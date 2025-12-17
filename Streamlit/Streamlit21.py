# Streamlit21.py
import streamlit as st
import pandas as pd
import altair as alt

st.title("📊 CSV 檔案上傳與分析")

# 上傳 CSV
uploaded_file = st.file_uploader("請選擇一個 CSV 檔案", type=["csv"])

if uploaded_file is not None:
    # 讀取 CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 原始資料")
    st.write(df)

    st.subheader("📈 簡單統計資訊")
    st.write(df.describe())

    st.subheader("📊 銷售總和")
    st.bar_chart(df.groupby("商品名稱")["銷售金額"].sum())

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X(
                "商品名稱",
                axis=alt.Axis(labelAngle=-45),
            ),
            y="銷售金額",
        )
    )
    st.altair_chart(chart, use_container_width=True)
