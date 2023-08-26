from dash import dash, Dash, Input, Output, callback, State, dcc
from dash.exceptions import PreventUpdate
from layout.components import *

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MINTY, dbc.icons.FONT_AWESOME, dbc_css],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)
server = app.server
app.title = "WUSTL DBBS PhD Stipend Pay Dates"
app._favicon = "assets/favicon.ico"

app.layout = dbc.Container(
    fluid=True,
    children=[dcc.Store(id="stored-data", storage_type="memory"), dash.page_container],
)


# Development Testing
if __name__ == "__main__":
    app.run(debug=True)

# Needed for server deployment later on
# if __name__ == "__main__":
#     server.run(host="0.0.0.0", port="8080")

# Author: Caelan Miller - 2023
