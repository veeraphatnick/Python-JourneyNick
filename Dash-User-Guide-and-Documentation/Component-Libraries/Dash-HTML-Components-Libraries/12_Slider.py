import dash
import dash_core_components as dcc 
import dash_html_components as html 
import dash_daq as daq

app = dash.Dash(__name__)

app.layout = html.Div([
    daq.Slider(
        id='my-daq-slider',
        value=17,
        min=0,
        max=100,
        targets={"25": {"label": "TARGET"}}
    )
])

if __name__=='__main__':
    app.run_server(debug=True)