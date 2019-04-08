import dash
import dash_core_components as dcc
import dash_html_components as html 

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Slider(
        min=-5,
        max=10,
        step=0.5,
        value=-3,
    ),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) for i in range(10)},
        value=5,
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)