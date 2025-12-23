# Dash20.py
from dash import Dash, Input, Output, callback, dcc, html

app = Dash()

my_input = dcc.Input(value='initial value', type='text')
my_output = html.Div()

app.layout = html.Div([
    html.H6("更改文字方塊中的值，即可查看回呼函數的實際效果！"),
    html.Div(["輸入文字: ",my_input]),
    html.Br(),
    my_output
])

@callback(
    Output(my_output, 'children'),
    Input(my_input, 'value')
)

def update_output_div(input_value):
    return f'輸出結果: {input_value}'

if __name__ == '__main__':
    app.run(port = 5000, debug = False)
