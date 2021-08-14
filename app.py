import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4("Insert a value between 0 - 1000 below"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)




if __name__ == '__main__':
    app.run_server(debug=True)