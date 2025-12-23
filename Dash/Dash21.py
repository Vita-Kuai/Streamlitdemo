# Dash21.py
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

import dash
from dash import Input, Output, dcc, html

# 創建應用實例
app = dash.Dash(__name__)

# 生成示例數據
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100, freq='D') #產生100天
df = pd.DataFrame({
    'date': dates,
    #亂數生成資料
    'sales': np.random.randint(1000, 2001, 100).cumsum(),
    # 1000-2000取100筆
    # .cumsum()做「累加」讓數值隨時間呈現成長趨勢👉 模擬「累積銷售額」
    'customers': np.random.randint(50, 200, 100),
    'region': np.random.choice(['北部', '中部', '南部', '東部'], 100),
    'category': np.random.choice(['電子產品', '服飾', '食品', '家居'], 100)
})

# 定義應用佈局
app.layout = html.Div([
    html.H1('銷售數據分析儀表板',
            style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 30}),

    # 控制面板
    html.Div([
        html.Div([
            # 使用者選「地區」 ALL代表不選
            html.Label('選擇地區:', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='region-filter',
                options=[{'label': '全部地區', 'value': 'ALL'}] +
                        [{'label': r, 'value': r} for r in df['region'].unique()],
                value='ALL',
                style={'width': '100%'}
            )
        ], style={'width': '30%', 'display': 'inline-block', 'marginRight': '3%'}),

        html.Div([
            # 商品分類篩選
            html.Label('選擇類別:', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='category-filter',
                options=[{'label': '全部類別', 'value': 'ALL'}] +
                        [{'label': c, 'value': c} for c in df['category'].unique()],
                value='ALL',
                style={'width': '100%'}
            )
        ], style={'width': '30%', 'display': 'inline-block', 'marginRight': '3%'}),

        # 控制資料的時間區間
        html.Div([
            html.Label('選擇日期範圍:', style={'fontWeight': 'bold'}),
            dcc.DatePickerRange(
                id='date-range',
                start_date=df['date'].min(),
                end_date=df['date'].max(),
                display_format='YYYY-MM-DD'
            )
        ], style={'width': '30%', 'display': 'inline-block'})
    ], style={'marginBottom': 30, 'padding': 20, 'backgroundColor': '#f8f9fa',
              'borderRadius': 10}),

    # 關鍵指標卡片 這三個是 callback 動態更新的數值顯示
    html.Div([
        html.Div([
            html.H4('總銷售額', style={'color': '#7f8c8d'}),
            html.H2(id='total-sales', style={'color': '#27ae60'})
        ], style={'width': '20%', 'display': 'inline-block', 'padding': 20,
                  'backgroundColor': '#ecf0f1', 'borderRadius': 10, 'marginRight': '3%'}),

        html.Div([
            html.H4('平均客戶數', style={'color': '#7f8c8d'}),
            html.H2(id='avg-customers', style={'color': '#3498db'})
        ], style={'width': '20%', 'display': 'inline-block', 'padding': 20,
                  'backgroundColor': '#ecf0f1', 'borderRadius': 10, 'marginRight': '3%'}),

        html.Div([
            html.H4('數據筆數', style={'color': '#7f8c8d'}),
            html.H2(id='data-count', style={'color': '#e74c3c'})
        ], style={'width': '20%', 'display': 'inline-block', 'padding': 20,
                  'backgroundColor': '#ecf0f1', 'borderRadius': 10})
    ], style={'marginBottom': 30}),

    # 圖表區域
    html.Div([
        html.Div([
            dcc.Graph(id='sales-trend') #趨勢圖
        ], style={'width': '65%', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(id='category-pie') #圓餅圖
        ], style={'width': '33%', 'display': 'inline-block', 'marginLeft': '2%'})
    ]),

    html.Div([
        dcc.Graph(id='customer-scatter') #散點圖
    ], style={'marginTop': 20}),

    # 數據表格
    html.Div([
        html.H3('詳細數據', style={'marginTop': 30}),
        html.Div(id='data-table') #表格
    ])

], style={'padding': 40, 'fontFamily': 'Arial, sans-serif'})


# 回調函數：更新所有圖表和指標
@app.callback(
    [Output('total-sales', 'children'),
     Output('avg-customers', 'children'),
     Output('data-count', 'children'),
     Output('sales-trend', 'figure'),
     Output('category-pie', 'figure'),
     Output('customer-scatter', 'figure'),
     Output('data-table', 'children')],
    [Input('region-filter', 'value'), # 地區
     Input('category-filter', 'value'), #類別
     Input('date-range', 'start_date'), #起始日期
     Input('date-range', 'end_date')]  #結束日期  任一改變，均會影響圖表
)
def update_dashboard(region, category, start_date, end_date): #四個input
    # 過濾數據
    filtered_df = df.copy()

    #過濾 地區
    if region != 'ALL': #如果不是全部地區
        filtered_df = filtered_df[filtered_df['region'] == region]  #只留下條件為 True 的列
    #過濾 類別
    if category != 'ALL':
        filtered_df = filtered_df[filtered_df['category'] == category]
    #過濾 日期
    filtered_df = filtered_df[
        (filtered_df['date'] >= start_date) &
        (filtered_df['date'] <= end_date)
    ]

    # 計算指標
    total_sales = f"${filtered_df['sales'].sum():,.0f}" #計算總額取整數
    avg_customers = f"{filtered_df['customers'].mean():.0f} 人" #計算特定地區分類的平均客戶/日
    data_count = f"{len(filtered_df)} 筆" #符合地區與分類、日期篩選的筆數

    # 銷售趨勢圖
    sales_fig = go.Figure()
    sales_fig.add_trace(go.Scatter(
        x=filtered_df['date'],
        y=filtered_df['sales'],
        mode='lines+markers',
        name='累計銷售額',
        line=dict(color='#3498db', width=3),
        marker=dict(size=6)
    ))
    sales_fig.update_layout(
        title='銷售趨勢',
        xaxis_title='日期',
        yaxis_title='銷售額 ($)',
        hovermode='x unified',
        template='plotly_white'
    )

    # 類別分布圓餅圖
    category_counts = filtered_df['category'].value_counts() # 計算每一個「不同值」出現的次數
    pie_fig = go.Figure(data=[go.Pie(
        labels=category_counts.index, # e.g. Index(['A', 'B', 'C'])
        values=category_counts.values, # e.g.array([10, 6, 4])
        hole=0.4
    )])
    pie_fig.update_layout(
        title='類別分布',
        template='plotly_white'
    )

    # 客戶數與銷售額散點圖
    scatter_fig = px.scatter(
        filtered_df,
        x='customers',
        y='sales',
        color='region',
        size='customers', # 氣泡大小 = 客戶數
        hover_data=['date', 'category'], # Plotly 自動幫你加的 hover 資訊有：x y color size
        title='客戶數 vs 銷售額'
    )
    scatter_fig.update_layout(template='plotly_white')

    # 數據表格
    table_data = filtered_df.tail(10).to_dict('records')
    table = html.Table([
        html.Thead(html.Tr([html.Th(col) for col in ['日期', '銷售額', '客戶數', '地區', '類別']])),
        html.Tbody([
            html.Tr([
                html.Td(row['date'].strftime('%Y-%m-%d')),
                html.Td(f"${row['sales']:,.0f}"),
                html.Td(row['customers']),
                html.Td(row['region']),
                html.Td(row['category'])
            ]) for row in table_data
        ])
    ], style={'width': '100%', 'borderCollapse': 'collapse', 'marginTop': 10,
              'border': '1px solid #ddd'})

    return total_sales, avg_customers, data_count, sales_fig, pie_fig, scatter_fig, table


# 運行應用
if __name__ == '__main__':
    app.run(port = 5000, debug = True)
