import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

df2 = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#FFFFFF',
    'text': '#111111'
}

app.layout = html.Div(
    [
        html.Div(
            style={'backgroundColor': colors['background']},
            # Headind
            children=[
                html.H1(
                    children='Hello Dash',
                    style={
                        'textAlign': 'center',
                        'color': colors['text'] 
                    }
                ),
                # Secondary title
                html.Div(
                    children='''
                        Dash: A web application framework for Python.''',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    }
                ),
                # Crate Bar Graph
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'plot_bgcolor': colors['background'],
                            'paper_bgcolor': colors['background'],
                            'font': {
                                'color': colors['text']
                            }   
                        }
                    }
                ),
                # Crate Line Graph
                dcc.Graph(
                    id='example-graph2',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'SF'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': u'Montréal'},
                        ],
                        'layout': {
                            'plot_bgcolor': colors['background'],
                            'paper_bgcolor': colors['background'],
                            'font': {
                                'color': colors['text']
                            }   
                        }
                    }
                ),
                # Show Table in Pandas
                html.Div(
                    children= html.H2(
                        children='US Agriculture Exports (2011)',
                        style={
                        'textAlign': 'center',
                        'color': colors['text'] 
                        }
                    )
                ),
                html.Div(
                    children=[
                        html.H4(
                            children='US Agriculture Exports (2011)'
                        ),
                    generate_table(df)
                    ]
                ),
                # Crate Scatter Plot
                html.Div(
                    children= html.H2(
                        children='Scatter Plot',
                        style={
                        'textAlign': 'center',
                        'color': colors['text'] 
                        }
                    )
                ),
                dcc.Graph(
                    id='life-exp-vs-gdp',
                    figure={
                        'data': [
                            go.Scatter(
                                x=df2[df2['continent'] == i]['gdp per capita'],
                                y=df2[df2['continent'] == i]['life expectancy'],
                                text=df2[df2['continent'] == i]['country'],
                                mode='markers',
                                opacity=0.7,
                                marker={
                                    'size': 15,
                                    'line': {'width': 0.5, 'color': 'white'}
                                },
                                name=i
                            ) for i in df2.continent.unique()
                        ],
                        'layout': go.Layout(
                            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                            yaxis={'title': 'Life Expectancy'},
                            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                            legend={'x': 0, 'y': 1},
                            hovermode='closest'
                        )
                    }
                )   
            ]
        ),
        html.Div(
            children= html.H2(
                children='Dash Core Component',
                style={
                'textAlign': 'center',
                'color': colors['text'] 
                }
            )
        ),
        html.Div(
            [
                html.Label('Dropdown'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value='MTL'
                ),

                html.Label('Multi-Select Dropdown'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value=['MTL', 'SF'],
                    multi=True
                ),

                html.Label('Radio Items'),
                dcc.RadioItems(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value='MTL'
                ),

                html.Label('Checkboxes'),
                dcc.Checklist(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    values=['MTL', 'SF']
                ),

                html.Label('Text Input'),
                dcc.Input(value='MTL', type='text'),

                html.Label('Slider'),
                dcc.Slider(
                    min=0,
                    max=9,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
                    value=5,
                ),
            ], 
            style={'columnCount': 2}
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)