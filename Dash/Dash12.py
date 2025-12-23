# Dash12.py
import dash_ag_grid as dag
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px

from dash import Dash, Input, Output, callback, dcc

df = pd.read_csv('https://raw.githubusercontent.com/johnsonshsu/pythondata/refs/heads/main/csv/gapminder_unfiltered.csv', encoding='utf-8')

app = Dash()

# 使用 MantineProvider 包裹整個應用程式
app.layout = dmc.MantineProvider(
    dmc.Container([
        dmc.Title("各洲別人口、預期壽命、人均GDP統計圖", c="blue", order=3),
        dmc.RadioGroup(
           dmc.Group([dmc.Radio(i, value=i) for i in  ['人口', '預期壽命', '人均GDP']]),
            id='my-dmc-radio-item',
            value='預期壽命',
            p="sm"
        ),
        dmc.SimpleGrid([
            dag.AgGrid(
                rowData=df.to_dict("records"),
                columnDefs=[{"field": i} for i in df.columns],
            ),
            dcc.Graph(figure={}, id='graph-placeholder')
        ], cols={"base": 1, "md": 2})
    ], fluid=True)
)

@callback(
    Output('graph-placeholder', 'figure'),
    Input('my-dmc-radio-item', 'value')
)

def update_graph(col_chosen):
    # 根據選項設定 Y 軸標籤
    y_labels = {
        '人口': '平均人口數',
        '預期壽命': '平均預期壽命(歲)',
        '人均GDP': '平均人均GDP(美元)'
    }

    fig = px.histogram(df, x='洲別', y=col_chosen, histfunc='avg')
    fig.update_yaxes(title_text=y_labels.get(col_chosen, col_chosen))
    return fig

if __name__ == '__main__':
    app.run(port = 5000, debug = False)
