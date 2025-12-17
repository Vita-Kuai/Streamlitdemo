# Streamlit15.py
import streamlit as st

# 頁面標題
st.title("123 健康科技集團", anchor="home")

st.markdown("---")
st.markdown("### 📌 快速導覽")
st.markdown("[公司簡介](#profile)")
st.markdown("[核心價值](#values)")
st.markdown("[產品與服務](#service)")
st.markdown("[合作夥伴](#partners)")
st.markdown("[公司願景](#vision)")
st.markdown("---")

# 主要內容
st.header("公司簡介", anchor="profile")
st.write(
    """
<h3>公司名稱：</h3>
123 健康科技集團
<h3>主要業務：</h3>
<ul>
<li>人工智慧解決方案開發</li>
<li>雲端系統整合與維運服務</li>
<li>企業資料分析與決策支援</li>
<li>行動應用程式設計與開發</li>
</ul>
<h5>成立時間：</h5> 2010 年
<h5>員工人數：</h5> 500 人
<h5>總部地點：</h5> 台北市信義區
<h5>分公司：</h5> 台中、高雄、新加坡、東京
<h5>網站：</h5> <a href="https://www.123healthtech.com" target="_blank">https://www.123healthtech.com</a>
""",
    unsafe_allow_html=True,
)
st.markdown("[回首頁](#home)")

st.header("核心價值：", anchor="values")
st.write(
    """
<ul>
<li>創新 (Innovation)</li>
<li>誠信 (Integrity)</li>
<li>專業 (Expertise)</li>
<li>共好 (Collaboration)</li>
</ul>
""",
    unsafe_allow_html=True,
)
st.markdown("[回首頁](#home)")

st.header("產品與服務", anchor="service")
st.write(
    """
<ul>
<li>AI 智慧型客服系統</li>
<li>雲端資料平台</li>
<li>行動商務解決方案</li>
<li>企業專屬巨量資料分析</li>
</ul>
""",
    unsafe_allow_html=True,
)
st.markdown("[回首頁](#home)")

st.header("合作夥伴", anchor="partners")
st.write(
    """
<ul>
<li>微軟 (Microsoft)</li>
<li>Google Cloud</li>
<li>台灣電信業者（中華電信、台灣大哥大)</li>
<li>金融與零售產業龍頭企業</li>
</ul>
""",
    unsafe_allow_html=True,
)
st.markdown("[回首頁](#home)")

st.header("公司願景", anchor="vision")
st.write(
    """
使命你跟員工講的時候，大家都覺得不錯。
接下來大家關心的是這家公司的願景，將來未來會變成什麼樣子？我會得到什麼好處？
這個願景是極其關鍵的。不關心願景就加入你們公司的員工，盡量少招聘。
他如果沒有問：「老闆，你們將來會變成什麼樣子？這個使命下去會變成什麼樣子？」
如果他對這些都不關心，他只關心下個月的工資在哪，你前面這幫員工找錯了。

你說什麼叫做願景？這個公司五年以後，可能會變成這個樣子、這個樣子；
十年以後，可能是這個樣子；二十年以後，可能是這個樣子。這個圖如果不出來，你是不可能有戰略的。
而這張圖跟這個願景必須匹配。你們不能說有一個偉大的使命，
但是願景是往另一邊走，員工都覺得矛盾。
那你自己也會發現，天天講使命、天天講願景的時候，你不講，員工不會記住。
你講多了以後，員工發現你做的跟說的是不是一樣。
""",
    unsafe_allow_html=True,
)
st.markdown("[回首頁](#home)")
