# Dash17.py
from dash import Dash, Input, Output, callback, dcc, html

external_stylesheets = ['https://raw.githubusercontent.com/johnsonshsu/pythondata/refs/heads/main/css/plotly.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    '美國': ['紐約市', '舊金山', '辛辛那提'],
    '加拿大': ['蒙特利爾', '多倫多', '渥太華']
}
app.layout = html.Div([
    dcc.RadioItems(
        list(all_options.keys()), # 把 all_options 這個字典裡的所有 key（鍵）拿出來，變成一個清單，當作 RadioItems 的選項」。
        '美國',
        id='countries-radio', # 選國家
    ),

    html.Hr(), #分隔線

    dcc.RadioItems(id='cities-radio'), # 選城市

    html.Hr(),

    html.Div(id='display-selected-values')
])

@callback(
    Output('cities-radio', 'options'),
    Input('countries-radio', 'value'))
def set_cities_options(selected_country): # 當 countries-radio 的 value 改變時執行
    return [{'label': i, 'value': i} for i in all_options[selected_country]] # all_options['美國'] -> ['紐約市', '舊金山', '辛辛那提']

# [
#    {'label': '紐約市', 'value': '紐約市'},
#    {'label': '舊金山', 'value': '舊金山'},
#    {'label': '辛辛那提', 'value': '辛辛那提'}
#]

@callback(
    Output('cities-radio', 'value'),
    Input('cities-radio', 'options'))
def set_cities_value(available_options): #available_options = Input('cities-radio', 'options')) = Output('cities-radio', 'options')(上一段)
    return available_options[0]['value'] # 讓畫面上自動選中第一個城市


@callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value'))
def set_display_children(selected_country, selected_city):
    return f'{selected_city} 是 {selected_country} 的一個城市'

if __name__ == '__main__':
    app.run(port = 5000, debug = False)
