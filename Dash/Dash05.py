# Dash05.py
import dash
from dash import dcc, html

app = dash.Dash()

app.layout = html.Div([
    html.H1("進階 Dash 折線圖範例(兩組數值)" , style={'textAlign':'center'}),

    dcc.Graph(
        id = 'First Dash Graph',
        figure = {
            'data': [
                {
                    'name': '管理部',
                    'type': 'line',
                    'mode': 'markers+lines+text',
                    'x': ['一月','二月','三月','四月','五月','六月'],
                    'y': [210,126,243,248,322,259],
                    'text': ['20','16','23','48','32','29']
                },
                {
                    'name': '業務部',
                    'type': 'line',
                    'mode': 'markers+lines+text',
                    'x': ['一月','二月','三月','四月','五月','六月'],
                    'y': [126,158,276,281,343,358],
                    'text': ['16','18','26','28','34','38']
                }
            ],
            'layout': {
                'title': {
                    'text': "2025 年上半年各部門加班時數統計圖",
                    'x':0.5,
                    'xanchor':'center'
                },
                'xaxis': {
                    'title': {'text': '月份'},
                    'showline': True,
                    'linewidth': 2,
                    'linecolor': 'black',
                    'mirror': True
                },
                'yaxis': {
                    'title': {'text': '加班時數 (單位: 小時)'},
                    'showline': True,
                    'linewidth': 2,
                    'linecolor': 'black',
                    'mirror': True
                }
            }
        }
    )
])

if __name__ == '__main__':
    ## port: 設定開出來的網路窗口，通常會有預設的，可以透過help()查看
    ## debug = True: 打開所有開發工具
    app.run(port = 5000, debug = False)
