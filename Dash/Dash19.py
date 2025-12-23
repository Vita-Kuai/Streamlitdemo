# Dash19.py
from dash import Dash, Input, Output, State, callback, dcc, html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='蒙特婁'),
    dcc.Input(id='input-2-state', type='text', value='加拿大'),
    html.Button(id='submit-button-state', n_clicks=0, children='提交'),
    html.Div(id='output-state')
])

@callback(Output('output-state', 'children'), # children：改變 id=output-state 元件裡顯示的內容
              Input('submit-button-state', 'n_clicks'), #Input：按下按鈕時（n_clicks 改變）觸發 callback
              State('input-1-state', 'value'), # State：不觸發 callback，只在 callback 執行時讀取目前的 value
              State('input-2-state', 'value'))
# 所以只有按下按鈕時會改變底下文字，打字進 input 時不會改變
def update_output(n_clicks, input1, input2):
    return f'''
        按鈕已被按下 {n_clicks} 次,
        第 1 個輸入值為 "{input1}",
        第 2 個輸入值為 "{input2}"
    '''

if __name__ == '__main__':
    app.run(port = 5000, debug = False)
