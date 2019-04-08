import dash 
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.ConfirmDialogProvider(
        children=html.Button(
            'Click Me',
        ),
        id='danger-danger',
        message='Danger danger! Are you sure you want to continue?'
    )
])

if __name__=='__main__':
    app.run_server(debug=True)