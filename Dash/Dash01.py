# Dash01.py
# 最簡單的 Dash 範例
# 引入 Dash 套件
from dash import Dash, html

## 啟動dash
app = Dash()

## 設定網頁介面
app.layout = [
        html.Div(
            children='Hello World')
    ]

if __name__ == '__main__':
    ## port: 設定開出來的網路窗口，通常會有預設的，可以透過help()查看
    ## debug = True: 打開所有開發工具
    app.run(port = 5000, debug = False)
