# Streamlit23.py
import os
import sqlite3

import pandas as pd

import streamlit as st


def get_data():
    # 取得腳本所在目錄
    script_dir = os.path.dirname(__file__)
    # 相對於腳本的上層目錄
    db_path = os.path.join(script_dir, "Demo.db")

    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM Users", conn)
    conn.close()
    return df


st.title("📊 SQLite 測試")

if st.button("顯示資料"):
    df = get_data()
    st.dataframe(df)
    st.success("資料載入成功！")

