## Dash02.py
import dash
from dash import html

app = dash.Dash()

app.layout = html.Div([
    html.H1("Dash 基本實作範例!!"),
    html.Div('Plotly 網頁框架 - Dash應用'),
    html.P('Dash 是以 Plotly.js 與 React.js 與Flask 為基礎建構的套件, 是一種低程式碼框架 (low-code framework) 的套件。')
])

if __name__ == '__main__':
    app.run(port = 5000, debug = False)
