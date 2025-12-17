# Streamlit07.py
import streamlit as st

# 標題格式
st.markdown("# 一級標題")
st.markdown("## 二級標題")
st.markdown("### 三級標題")
st.markdown("#### 四級標題")
st.markdown("##### 五級標題")
st.markdown("###### 六級標題")

# 分隔線
st.markdown("***")
st.markdown("普通文字")
st.markdown(":red[紅色文字]")

# 文字
st.markdown("*斜體文字*")
st.markdown("_斜體文字_")
st.markdown("**粗體文字**")
st.markdown("__粗體文字__")
st.markdown("***粗斜體文字***")
st.markdown("___粗斜體文字___")
st.markdown("~~刪除線文字~~")
st.markdown("`單行程式碼文字`")
st.markdown("""
```python
# 多行程式碼區塊範例
print("Hello, World!")

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
```""")
st.markdown("> 引用文字")

# 分隔線
st.markdown("***")
# 無序列表
st.markdown("""- Python
- Java
- C#""")

# 分隔線
st.markdown("***")
# 有序列表
st.markdown("""1. 第1項
2. 第2項
3. 第3項""")

# 分隔線
st.markdown("***")
# 表格
st.markdown("""
|標頭 | 標頭2 |
| :-: | :-: |
| 儲存格1|儲存格2 |
| 儲存格3|儲存格4|""")
