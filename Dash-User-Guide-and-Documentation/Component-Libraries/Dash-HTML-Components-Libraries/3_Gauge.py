import dash
import dash_core_components as dcc 
import dash_html_components as html 
import dash_daq as daq

app = dash.Dash(__name__)

app.layout = html.Div([
    daq.Gauge(
        id='my-daq-gauge',
        min=0,
        max=10,
        value=6
    )
])

if __name__=='__main__':
    app.run_server(debug=True)