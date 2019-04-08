import dash
import dash_core_components as dcc 
import dash_html_components as html 

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
            ],
        value='MTL'
        ),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL',
        labelStyle={'display': 'inline-block'}
    )
])

if __name__ =='__main__':
    app.run_server(debug=True)