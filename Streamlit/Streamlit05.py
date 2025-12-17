# Streamlit05.py
import streamlit as st  # 匯入 Streamlit 並用 st 代替

st.subheader("Python 程式區塊")

# 建立要顯示的 Python 程式區塊的內容
python_code = """def hello():
print ("你好 ,Streamlit !")
"""

# 建立一個程式區塊 ,用於展示 python_code 的內容
# 將 language 設定為 None , 即該程式區塊無語法突顯
st.code(python_code, language=None)

# 建立一個程式區塊,用於展示 python_code 的內容
# language 為預設 , 即該程式區塊以 Python 語法突顯
st.code(python_code)

# 建立一個程式區塊 ,用於展示 python_code 的內容
# language 為頑設 , 即該程式區塊以 python 語法突顯
# 將 line_numbers 設定為 True , 即該程式區塊有行號
st.code(python_code, line_numbers=True)

st.subheader("Java 程式區塊")

# 建立要顯示的 Java 程式區塊的內容
java_code = """public class Hello {
    public static void main (String[] args) {
        System.out.println("你好 ! Streamlit !");
    }
}
"""

# 建立一個程式區塊'用於展示 java_code 的內容
# 將 1angtage 設定為 Java , 即該程式區塊以 Java 語法突飄
st.code(java_code, language="java")
st.subheader(" Javascript 程式區塊")

# 建立要顯示的 Javascript 程式區塊的內容
javascript_code = """<p id="demo"></p>
<script>
    document.getElementById("demo").innerHTML = "你好 ! Streamlit !";
</script>
"""

# 建立一個程式區塊 ,用於展示 javascript_code 的內容
# 將 language 設定為 javascript ' 即該程式區塊以 javascript 諮法突顯
st.code(javascript_code, language="javascript")
