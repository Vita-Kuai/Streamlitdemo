# Streamlit02.py
# 匯入 streamlit 並用 st 代表它
import streamlit as st
# 這裏為了演示建立了多個標題展示元素

# 1. 建立一個標題展示元素:內容是全英文的 ,預設錨點為 first-title
st.title("First Title")

# 2. 建立一個標題展示元素 ,內容是全中文的，如不定義 anchor 參數 , 則無錨點
st.title("中文標題")

# 3. 建立一個標題展示元素 ,內容是中英文混雜的，預設的錨點是英文部分 ,即英文單字 chinese
st.title("這是 chinese 標題")

# 4. 建立一個標題展示元素並增加了錨點
st.title("這個標題有設定錨點", anchor="fourth")

# 5. 建立一個標題展示元素並增加了錨點和工具提示
st.title("這個標題有設定錨點及工具提示", anchor="fifth", help="工具提示")

# 6. 建立一個標題展示元素內容使用了 Markdown 語法和表情符號並增加了錨點和工具提示
st.title(
    "這個標題使用了 Markdown 語法和表情符號並增加了錨點和工具提示 :sunglasses:",
    anchor="sixth",
)
