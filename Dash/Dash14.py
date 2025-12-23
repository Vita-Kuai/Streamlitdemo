# Dash14.py
import pandas as pd
import plotly.express as px

from dash import Dash, Input, Output, callback, dcc, html

# 讀取資料
df = pd.read_csv('https://raw.githubusercontent.com/johnsonshsu/pythondata/refs/heads/main/csv/gapminder_unfiltered.csv', encoding='utf-8')

app = Dash()

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    html.Div([
        dcc.Slider(
            df['年份'].min(),
            df['年份'].max(),
            step=1,
            value=df['年份'].min(),
            marks={str(年份): {'label': str(年份), 'style': {'transform': 'rotate(-45deg)', 'white-space': 'nowrap'}} for 年份 in df['年份'].unique()},
            id='year-slider'
        )
    ], style={'margin-top': '30px', 'margin-bottom': '30px'})
])

@callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))

def update_figure(selected_year):
    filtered_df = df[df.年份 == selected_year]

    fig = px.scatter(filtered_df, x="人均GDP", y="預期壽命",
                     size="人口", color="洲別", hover_name="國家",
                     log_x=True, size_max=55)

    fig.update_layout(
        title={
            'text': f'{selected_year}年 各國人均GDP與預期壽命關係圖',
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis={'tickangle': 0},
        transition_duration=500
    )

    return fig

if __name__ == '__main__':
    app.run(port = 5000, debug = False)
