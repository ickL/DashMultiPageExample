import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash
from app import server, app
from Apps.GlobalFunctions import ImportApps #import loading and logging functions  from a subfolder

layoutList = ImportApps.AllApps(defaultApp="AppName1") #generate page list and establish default page

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=layoutList['Default'].Page),    
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    pathnameUpper = pathname.upper() #user to be able to type in the address with whatever capitalization they choose.
    if len(pathnameUpper) > 1: #check if at home/default page before looking through layoutList for correct page to be on
        site = False #variable to check if correct site is found, else returning 404 page
        for i in layoutList:
            if pathnameUpper == "/APPS/" + i.upper():
                site = True
                return layoutList[i].Page
        if site == False:
            return html.Div([html.H4("404 - Page Not Found")])
    else:
        return layoutList["Default"].Page

if __name__ == '__main__':
    app.run_server(debug=True)



