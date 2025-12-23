# Dash15.py
import pandas as pd
import plotly.express as px

from dash import Dash, Input, Output, callback, dcc, html

app = Dash()

df = pd.read_csv('https://raw.githubusercontent.com/johnsonshsu/pythondata/refs/heads/main/csv/country_indicators.csv')

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown( # 下拉選單
                df['指標名稱'].unique(),
                '農業增加值(佔GDP百分比)',
                id='xaxis-column'
            ),
            dcc.RadioItems( # 單選
                ['Linear', 'Log'],
                'Linear',
                id='xaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown( # 下拉選單
                df['指標名稱'].unique(),
                '總生育率(每名婦女生育數)',
                id='yaxis-column'
            ),
            dcc.RadioItems( # 單選
                ['Linear', 'Log'],
                'Linear',
                id='yaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

    dcc.Slider(
        df['年份'].min(),
        df['年份'].max(),
        step=1,
        id='year--slider',
        value=df['年份'].max(),
        marks={str(年份): str(年份) for 年份 in df['年份'].unique()},

    )
])


@callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
    Input('year--slider', 'value'))
# 會「依照順序」對應到函式參數
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df[df['年份'] == year_value] # 只保留指定年份的資料 dff 是「某一年」的所有指標、所有地區

    # 分別取得 x 軸和 y 軸的資料
    dff_x = dff[dff['指標名稱'] == xaxis_column_name]
    dff_y = dff[dff['指標名稱'] == yaxis_column_name]

    # 合併兩個資料集,使用地區名稱作為鍵
    dff_merged = pd.merge(
        dff_x[['地區名稱', '數值']].rename(columns={'數值': 'x'}), # 數值那一欄rename成 x
        dff_y[['地區名稱', '數值']].rename(columns={'數值': 'y'}), # 數值那一欄rename成 y
        on='地區名稱'
    )
    #地區名稱	x	y
    #台北市	    260	720
    #畫散佈圖（scatter plot）最理想的資料格式

    fig = px.scatter(dff_merged, x='x', y='y', hover_name='地區名稱') # 調整圖表邊界（單位是像素）：
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest') # 滑鼠靠近哪個點 就顯示最近的那個點的資訊

    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    return fig # fig 被回傳 Dash 把它放進Output


if __name__ == '__main__':
    app.run(debug=True)
