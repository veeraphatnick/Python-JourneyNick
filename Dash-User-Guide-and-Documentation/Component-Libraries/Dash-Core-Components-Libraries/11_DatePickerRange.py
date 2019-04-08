import dash
import dash_core_components as dcc 
import dash_html_components as html 
from datetime import datetime as dt

app = dash.Dash(__name__)

app.layout = html.Div([
   dcc.DatePickerRange(
        id='date-picker-range',
        start_date=dt(1997, 5, 3),
        end_date_placeholder_text='Select a date!'
    )
])

if __name__=='__main__':
    app.run_server(debug=True)