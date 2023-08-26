from layout.components import *
from dash import Dash, html, Input, Output
from dash.exceptions import PreventUpdate
from calendar_generation import retrieve_current_date
from scraping_utils import processed_excel_file

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MINTY, dbc.icons.FONT_AWESOME, dbc_css],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)
# server = app.server
app._favicon = "assets/favicon.ico"
app.title = "WUSTL DBBS Stipend Pay Dates"
app.layout = dbc.Container(
    fluid=False,
    children=[
        site_nav,
        dbc.Row(
            className="justify-content-center align-items-center",
            id="body-content",
            children=[
                date_query_button,
            ],
        ),
        page_footer,
    ],
)


@app.callback(
    Output(component_id="body-content", component_property="children"),
    Input(component_id="date-btn", component_property="n_clicks"),
    prevent_initial_call=True,
)
def update_date_header(n_clicks):
    current_date = retrieve_current_date()
    paydate_dataframe = processed_excel_file
    if n_clicks is None:
        raise PreventUpdate
    else:
        result_component = html.Div(
            children=[
                html.H1(
                    f"Today's Date: {current_date}", style={"text-align": "center"}
                ),
                dbc.Table.from_dataframe(
                    paydate_dataframe, striped=True, bordered=True, hover=True
                ),
            ]
        )
        return result_component


# Development Testing
if __name__ == "__main__":
    app.run(debug=True)

# Needed for server deployment later on
# if __name__ == "__main__":
#     server.run(host="0.0.0.0", port="8080")

# Author: Caelan Miller - 2023
