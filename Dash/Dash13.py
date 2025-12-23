# Dash13.py
from dash import Dash, Input, Output, callback, dcc, html

app = Dash()

app.layout = html.Div([
    html.H3("更改文字方塊中的值，即可查看回呼函數的實際效果！", style={'color': 'green'}),
    html.Div([
        "請輸入文字: ",
        dcc.Input(id='my-input', value='王大明', type='text' , style={'fontSize': '24px'})
    ] , style={'fontSize': '24px'}),
    html.Br(),
    html.Div(id='my-output', style={'fontSize': '24px', 'color': 'blue'}),

])


@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)

def update_output_div(input_value):
    return f'您輸入的文字是: {input_value}'

if __name__ == '__main__':
    app.run(port = 5000, debug = False)
