# Streamlit17.py
import streamlit as st

st.title("史密斯任務")
st.header("史密斯任務")
st.subheader("是一部 2005 年美國喜劇動作片，由布萊德·彼特與安潔莉娜·裘莉領銜主演。")
st.write("發行日期：2005年6月28日")
st.write(
    """約翰是一名建築公司高管，珍是一名技術支持顧問，他們在婚姻輔導中回答問題。他們結婚已有五到六年，
    但他們的婚姻現在正處於危機之中。他們談到最初在哥倫比亞波哥大相遇的情形，
    聲稱為了避免被當地當局質疑而在一起；兩人相愛並結婚。"""
)
st.write(
    "實際上，約翰和珍都是熟練的外勤特工，分別為不同的合約殺手公司工作；他們都是各自領域中的佼佼者，擅長隱瞞真實職業。"
)
st.markdown(
    "[維基百科](https://zh.wikipedia.org/wiki/%E5%8F%B2%E5%AF%86%E6%96%AF%E4%BB%BB%E5%8B%99)"
)
st.caption("資料來源：維基百科")
code = """
list1 = [12, 3, 4, 15];s=0
for i,a in enumerate(list1):
  s+=a
print(s)
"""
st.code(
    code,
    language="python",
    line_numbers=True,
    wrap_lines=False,
    height="content",
    width="stretch",
)
