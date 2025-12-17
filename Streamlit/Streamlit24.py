# Streamlit24.py
import os
import sqlite3

import pandas as pd

import streamlit as st

st.set_page_config(page_title="數位儀表板", layout="wide")


# 讀取資料
def get_data():
    # 取得腳本所在目錄
    script_dir = os.path.dirname(__file__)
    # 相對於腳本的上層目錄
    db_path = os.path.join(script_dir, "Demo.db")

    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM Users", conn)
    conn.close()
    return df


# 新增資料
def add_user(name, gender):
    # 取得腳本所在目錄
    script_dir = os.path.dirname(__file__)
    # 相對於腳本的上層目錄
    db_path = os.path.join(script_dir, "Demo.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (UserName, Gender) VALUES (?, ?)", (name, gender))
    conn.commit()
    conn.close()


st.title("📊 使用者數位儀表板")

# Sidebar 表單
with st.sidebar:
    st.header("新增使用者")
    name = st.text_input("姓名")
    gender = st.selectbox("性別", ["男", "女"])
    if st.button("新增"):
        add_user(name, gender)
        st.success("已新增成功！")

# 主畫面
df = get_data()

col1, col2 = st.columns(2)

with col1:
    st.subheader("使用者清單")
    st.dataframe(df)

with col2:
    if not df.empty:
        st.subheader("性別統計")
        gender_counts = df["Gender"].value_counts()
        st.bar_chart(gender_counts)

# 指標
st.subheader("統計指標")
if not df.empty:
    col1, col2, col3 = st.columns(3)
    col1.metric("總人數", len(df))
    col2.metric("男性人數", (df["Gender"] == "男").sum())
    col3.metric("女性人數", (df["Gender"] == "女").sum())
