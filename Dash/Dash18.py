# Dash18.py
from dash import Dash, Input, Output, callback, dcc, html

external_stylesheets = ['https://raw.githubusercontent.com/johnsonshsu/pythondata/refs/heads/main/css/plotly.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id="input-1", type="text", value="蒙特婁"),
    dcc.Input(id="input-2", type="text", value="加拿大"),
    html.Div(id="number-output"),
])

@callback(
    Output("number-output", "children"),
    Input("input-1", "value"),
    Input("input-2", "value"),
)
def update_output(input1, input2):
    return f'第 1 個輸入值為 "{input1}" 和第 2 個輸入值為 "{input2}"'

if __name__ == '__main__':
    app.run(port = 5000, debug = False)
