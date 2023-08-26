from layout.components import dbc, date_query_searchbar, page_footer
from dash import dcc, register_page, callback, Input, Output
from dash.exceptions import PreventUpdate
from calendar_generation import retrieve_current_date

register_page(__name__, path="/", title="WUSTL DBBS PhD Pay Dates")

layout = dbc.Container(
    fluid=True,
    children=[
        dcc.Location(id="page-url", refresh=True),
        date_query_searchbar,
        page_footer
    ],
)


@callback(
    Output(component_id="stored-data", component_property="data"),
    Input(component_id="date-btn", component_property="n_clicks"),
    prevent_initial_call=True,
)
def store_current_date(n_clicks: int):
    if n_clicks is None:
        raise PreventUpdate
    else :
        current_date = retrieve_current_date()
        return current_date
