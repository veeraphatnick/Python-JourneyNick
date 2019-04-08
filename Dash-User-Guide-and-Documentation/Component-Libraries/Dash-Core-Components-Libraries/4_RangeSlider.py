import dash
import dash_core_components as dcc 
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.RangeSlider(
        count=1,
        min=-5,
        max=10,
        step=0.5,
        value=[-3, 7]
    ),
    dcc.RangeSlider(
        marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
        min=-5,
        max=6,
        value=[-3, 4]
    )
])

if __name__=='__main__':
    app.run_server(debug=True)