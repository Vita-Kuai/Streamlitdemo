# Dash06.py
import dash_ag_grid as dag
import pandas as pd

from dash import Dash, html

# 讀取 GitHub 上 CSV 檔案
df = pd.read_csv('https://raw.githubusercontent.com/johnsonshsu/pythondata/refs/heads/main/csv/gapminder_unfiltered.csv', encoding='utf-8')

app = Dash()

app.layout = [
    html.Div(children='2007年各國人口資料', style={'textAlign':'center', 'fontSize':24, 'marginBottom':20}),
    html.Hr(),

    # 使用 Ag-Grid 顯示資料表格
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{"field": i} for i in df.columns]
    )
]

if __name__ == '__main__':
    app.run(port = 5000, debug = False)
