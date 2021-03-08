import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import sys

##importing a file from the DashboardData folder. This can be used in the callbacks, layout, or main file
#name = "AppName2"
#dataDirectory = sys.argv[0].replace("index.py", "Apps\\" + name + "\\DashboardData\\")
#file = open(dataDirectory + "TextFile.txt", "r")
#print(file.read())

layout = html.Div([
    html.H3("App2!", id="TextWrittenApp2"),
    dcc.Link('Navigate to "AppName1"', href='/Apps/AppName1'),
    html.Br(),
    html.Br(),
    dbc.Button("Button Callback Test!!", id="ButtonCallbackApp2")
])
