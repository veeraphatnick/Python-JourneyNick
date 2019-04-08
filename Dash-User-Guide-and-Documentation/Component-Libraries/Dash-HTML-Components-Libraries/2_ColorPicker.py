import dash
import dash_core_components as dcc 
import dash_html_components as html 
import dash_daq as daq

app = dash.Dash(__name__)

app.layout = html.Div([
    daq.ColorPicker(
        id='my-daq-colorpicker',
        label="ColorPicker"
    )
])

if __name__=='__main__':
    app.run_server(debug=True)