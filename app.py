import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
    dcc.Link('Main Menu', href='/page-1'),
    html.Br(),
    dcc.Link('Results Page', href='/page-2'),
])

page_1_layout = html.Div([
    html.H1('Main Menu'),
    html.H4("Insert a value between 0 - 1000 below"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='', type='number', min=0, max=1000, persistence=True, persistence_type='memory')
    ]),
    html.Br(),
    html.Div(id='my-output'),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go to Results Page', href='/page-2'),
    html.Br(),
    dcc.Link('Home', href='/'),
])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)


@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)


page_2_layout = html.Div([
    html.H1('Results Page'),

    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Main Menu', href='/page-1'),
    html.Br(),
    dcc.Link('Home', href='/')
])

@app.callback(dash.dependencies.Output('page-2-content', 'children'),
              [dash.dependencies.Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected {}'.format(value)


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page


if __name__ == '__main__':
    app.run_server(debug=True)