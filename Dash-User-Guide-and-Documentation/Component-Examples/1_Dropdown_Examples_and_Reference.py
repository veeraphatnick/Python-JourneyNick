import dash
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC',

        # Multi-Value Dropdown
        #value=['MTL','NYC']
        #multi=True
        
        # Disable Search
        #searchable=False

        # Dropdown Clear
        #clearable=False

        # Placeholder Text
        #placeholder="Select a city"

        # Disable Dropdown
        #disabled=True

        # Disable Options
        #options=[
        #    {'label': 'New York City', 'value': 'NYC', 'disabled': True},
        #    {'label': 'Montreal', 'value': 'MTL'},
        #    {'label': 'San Francisco', 'value': 'SF', 'disabled': True}
        #],
        
    ),
    html.Div(id='output-container')
])
@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)