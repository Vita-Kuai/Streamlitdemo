# Dash04.py
import dash
from dash import dcc, html

app = dash.Dash()

app.layout = html.Div([
    html.H1("進階 Dash 折線圖範例" , style={'textAlign':'center'}),

    dcc.Graph(
        id = 'First Dash Graph',
        figure = {
            'data': [{
                'type': 'line',
                'mode': 'lines+markers+text',
                'x': ['一月','二月','三月','四月','五月','六月' ,'七月','八月','九月','十月','十一月','十二月'],
                'y': [20,16,23,48,32,29, 35, 40, 45, 50, 55, 60],
                'text': ['20','16','23','48','32','29', '35', '40', '45', '50', '55', '60'],
                'name': '手機銷售量',
                'textposition': 'top center',
                'marker': {
                    'color': 'rgb(255,100,102)',
                    'line': {'width':2,'color':'rgb(0,0,0)'}
                }
            }],
            'layout': {
                'title': {
                    'text': '2025 年手機銷售量統計圖',
                    'x': 0.5,
                    'xanchor': 'center'
                },
                'plot_bgcolor': 'rgba(240, 240, 240, 0.5)',
                'paper_bgcolor': 'white',
                'margin': {'l': 60, 'r': 40, 't': 80, 'b': 60},
                'xaxis': {
                    'title': {'text': '月份'},
                    'showline': True,
                    'linewidth': 2,
                    'linecolor': 'black',
                    'mirror': True
                },
                'yaxis': {
                    'title': {'text': '銷售量 (單位: 支)'},
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
    app.run(port = 5000, debug = False)
