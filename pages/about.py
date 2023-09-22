from dash import register_page, callback, Input, Output
from layout.components import dbc, site_nav, about_page_content, page_footer
from dash.exceptions import PreventUpdate

register_page(__name__, path="/about")

layout = dbc.Container(
    id="about-container",
    fluid=True,
    children=[site_nav, about_page_content, page_footer],
)


@callback(
    Output(component_id="about-page", component_property="children"),
    Input(component_id="about-link", component_property="n_clicks"),
    prevent_initial_call=True,
)
def display_about_page(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return about_page_content
