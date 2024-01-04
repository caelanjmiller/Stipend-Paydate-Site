from dash import Dash, dash
from layout.components import dbc

bootstrap_css = (
    "https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
)
app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.icons.FONT_AWESOME, bootstrap_css],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)
server = app.server
app._favicon = "assets/favicon.ico"
app.title = "When Am I Getting Paid?"
app.layout = dbc.Container(
    id="main-container", fluid=False, children=[dash.page_container]
)

# Development Testing
if __name__ == "__main__":
    app.run(debug=True)

# Author: Caelan Miller - 2023
