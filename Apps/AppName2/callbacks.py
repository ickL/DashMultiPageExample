from dash.dependencies import Input, Output, State
import importlib
app = importlib.import_module("app").app

@app.callback(Output('TextWrittenApp2', 'children'),
              [Input('ButtonCallbackApp2', 'n_clicks')])
def ChangeTextColor(click):
    if click is not None:
        return "ButtonPressed " + str(click) + " times!"
    else:
        return "App2!"
