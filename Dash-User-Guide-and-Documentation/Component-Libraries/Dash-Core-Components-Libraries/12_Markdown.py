import dash
import dash_core_components as dcc 
import dash_html_components as html 

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Markdown('''
        #### Dash and Markdown
        Dash supports [Markdown](http://commonmark.org/help).
        Markdown is a simple way to write and format text.
        It includes a syntax for things like **bold text** and *italics*,
        [links](http://commonmark.org/help), inline `code` snippets, lists,
        quotes, and more.
        '''
    )
])

if __name__=='__main__':
    app.run_server(debug=True)