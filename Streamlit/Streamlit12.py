# Streamlit12.py
import streamlit as st  # 匯入 streamlit 並用 st 代表它
import json  # 匯入 JSON 函式庫

# 使用 open() 函式, 讀取 json_data. json 檔案
# 並將編碼指定為 utf-8 (因為檔案中包含中文)
with open("Streamlit/json_data.json", "r", encoding="utf-8") as f:
    my_obj = json.load(f)
    st.subheader("來自 JSON 檔案的資料")
    st.json(my_obj)

my_string = """[
{"name":"王鑫", "city":"臨汾"},
{"name":"Bob" , "city":"london"}
]"""

st.subheader("來自 Python 字串")
st.json(my_string, expanded=False)
