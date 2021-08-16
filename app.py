import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


print(dcc.__version__)
app = dash.Dash(__name__, suppress_callback_exceptions=True)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#CBC3E3',
}

app.config.suppress_callback_exceptions = True

index_page = html.Div(
    id='index_page',
    children=[
        dcc.Link('Go to Main Page', href='/page-1'),
        html.Br(),
        dcc.Link('Go to Report Page', href='/page-2'),
    ],
    style={'display': 'block', 'line-height': '0', 'height': '0', 'overflow': 'hidden',
           'backgroundColor': colors['background']}
)

page_1_layout = html.Div(
    # I added this id attribute
    id='page_1_layout',
    children=[
        html.H1('Main Page'),
        html.H4("Insert a value between 0 - 1000 below"),
        html.Div([
            "Input: ",
            dcc.Input(id='my-input', value='', type='number', min=0, max=1000,
                      persistence=True, persistence_type='memory')
        ]),
        html.Br(),
        html.Div(id='my-output'),

        html.Div(id='page-1-content'),
        html.Br(),
        dcc.Link('Go to Report', href='/page-2'),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
    ],
    # I added this style attribute
    style={'display': 'block', 'line-height': '0', 'height': '0', 'overflow': 'hidden'}

)

page_2_layout = html.Div(
    # I added this id attribute
    id='page_2_layout',
    children=[
        html.H1('Report Page'),
        html.Div(id='page-2-content'),
        html.Br(),
        dcc.Link('Go to Main Page', href='/page-1'),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
    ],
    # I added this style attribute
    style={'display': 'block', 'line-height': '0', 'height': '0', 'overflow': 'hidden'}
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content',
             # I added this children attribute
             children=[index_page, page_1_layout, page_2_layout]
             )
])


# Update the index
@app.callback(
    [dash.dependencies.Output(page, 'style') for page in ['index_page', 'page_1_layout', 'page_2_layout']],
    # I turned the output into a list of pages
    [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    return_value = [{'display': 'block', 'line-height': '0', 'height': '0', 'overflow': 'hidden'} for _ in range(3)]

    if pathname == '/page-1':
        return_value[1] = {'height': 'auto', 'display': 'inline-block'}
        return return_value
    elif pathname == '/page-2':
        return_value[2] = {'height': 'auto', 'display': 'inline-block'}
        return return_value
    else:
        return_value[0] = {'height': 'auto', 'display': 'inline-block'}
        return return_value


@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('my-input', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)


@app.callback(Output('page-2-content', 'children'),
              [Input('my-input', 'value')])
def page_2(value):
    return 'The all important value driving our business decisions is "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
