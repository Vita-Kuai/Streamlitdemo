# Streamlit08.py
import streamlit as st  # 匯入 Streaml it 並用 st 代表它
import sympy  # 匯入 SymPy

# 顯示 Larex 字串
st.subheader("顯示 Larex 字串")
st.latex(r"""\textstyle\sum_{k=0}^{n-1} cx^k =
c \left(\frac{l-x^{n}}{l-x}\right)""")

# 顯示 Sympy 運算式
st.subheader("顯示 Symey 運算式")

# 將% 定義為符號 x
x = sympy.Symbol("x")
# expr 為求 x 的平方根
expr = sympy.sqrt(x)
# 顯示 expr 運算式
st.latex(expr)
