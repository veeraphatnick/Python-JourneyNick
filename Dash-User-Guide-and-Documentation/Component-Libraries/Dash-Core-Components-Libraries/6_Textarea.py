import dash
import dash_core_components as dcc 
import dash_html_components as html 

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Textarea(
        placeholder='Enter a value...',
        value='This is a TextArea component',
        style={'width': '100%'}
    )
])

if __name__ =='__main__':
    app.run_server(debug=True)