import dash

app = dash.Dash(__name__, meta_tags=[{'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge,chrome=1'}])

server = app.server
app.config.suppress_callback_exceptions = True
app.title = "MultiPage Dashboard Template"


