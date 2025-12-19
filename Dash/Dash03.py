## Dash03.py
import dash
from dash import dcc, html

app = dash.Dash()

app.layout = html.Div(children = [
    html.H1(children = "基礎 Dash 柱狀圖範例", style = { 'textAlign': 'center', 'color': '#46A3FF' }),
    html.Div('Plotly 網頁框架 — Dash 的應用',  style = dict(textAlign = 'center', color = 'blue')),
    html.P('Dash 是以 Plotly.js 與 React.js 與Flask 為基礎建構的套件, 是一種低程式碼框架 (low-code framework) 的套件。'),

    dcc.Graph(
        id = 'Dash Chart',
        figure = {
            'data' : [
                {'x': ['一月','二月','三月','四月','五月','六月'], 'y': [2,6,6,8,20,18], 'type': 'bar', 'name': '平板電腦銷售量'},
                {'x': ['一月','二月','三月','四月','五月','六月'], 'y': [4,8,10,18,28,28], 'type':'bar', 'name': '筆記型電腦銷售量'}
            ],
            'layout': {
                'title': {
                    'text': '2025 年上半年電子產品銷售量統計圖',
                    'x': 0.5,
                    'xanchor': 'center'
                },
                'xaxis': {'title': {'text': '月份'}},
                'yaxis': {'title': {'text': '銷售量 (單位: 支)'}},
                'plot_bgcolor': '#66B3FF',
                'paper_bgcolor': '#D8D8EB',
                'font': dict(color = '#484891')
            }
        }
    )
])

if __name__ == '__main__':
    app.run(port = 5000, debug = False)
