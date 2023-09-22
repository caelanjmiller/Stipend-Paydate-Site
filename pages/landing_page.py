from dash import dcc, html, register_page, callback, Input, Output
from layout.components import (
    dbc,
    site_jumbotron,
    site_nav,
    date_query_button,
    download_calendar_button,
    page_footer,
)
from calendar_generation import *
from scraping_utils import processed_excel_file
from dash.exceptions import PreventUpdate


register_page(__name__, path="/", title="When Am I Getting Paid?")

layout = dbc.Container(
    fluid=True,
    children=[
        site_nav,
        dcc.Download(id="generated-calendar"),
        dbc.Row(id="body-content", children=[site_jumbotron, date_query_button]),
        page_footer,
    ],
)


@callback(
    Output(component_id="body-content", component_property="children"),
    Input(component_id="date-btn", component_property="n_clicks"),
    prevent_initial_call=True,
)
def update_body_content(n_clicks):
    current_date = retrieve_current_date()
    current_date_int = date_string_to_int(current_date, "%m/%d/%Y", "%m%d%Y")
    paydate_dataframe = processed_excel_file
    next_pay_date = check_closest_paydate(paydate_dataframe, current_date_int)
    if n_clicks is None:
        raise PreventUpdate
    else:
        result_component = html.Div(
            children=[
                html.H2(
                    f"Today's Date: {current_date}", style={"text-align": "center"}
                ),
                html.H1(
                    f"Next Pay Date: {next_pay_date}",
                    style={"text-align": "center", "color": "#e83e8c"},
                ),
                dbc.Table.from_dataframe(
                    paydate_dataframe, striped=True, bordered=True, hover=True
                ),
                download_calendar_button,
            ]
        )
        return result_component


@callback(
    Output(component_id="generated-calendar", component_property="data"),
    Input(component_id="download-btn", component_property="n_clicks"),
    prevent_initial_call=True,
)
def download_generated_calendar(n_clicks):
    paydate_dataframe = processed_excel_file
    final_calendar = calendar_generation(paydate_dataframe)
    if n_clicks is None:
        raise PreventUpdate
    else:
        print(final_calendar.to_ical().decode("utf-8"))
        # return dict(content=final_calendar, filename="stipend_paydates.ics")
        return
