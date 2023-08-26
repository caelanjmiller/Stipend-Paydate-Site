import dash_bootstrap_components as dbc
from dash import html, dcc

money_icon = html.I(className="fa-solid fa-sack-dollar")

date_query_searchbar = dbc.Row(
    className="query-height justify-content-center align-items-center",
    children=[
        dbc.Col(
            children=[
                html.H1(
                    id="header-title",
                    children=[
                        money_icon,
                        "When Am I Getting Paid?",
                        money_icon,
                    ],
                    style={"text-align": "center"},
                ),
                dbc.Button(
                    "Click For Next Pay Date",
                    color="primary",
                    className="d-grid gap-2 col-6 mx-auto",
                    id="date-btn",
                ),
            ]
        )
    ],
)

page_footer = dbc.Row(
    className="justify-content-center align-items-center",
    id="page-footer",
    children=[
        html.A(
            children=[
                "Caelan Miller",
                html.I(className="fa-brands fa-github", style={"margin": "auto"}),
            ],
            target="_blank",
            href="https://github.com/caelanjmiller",
            id="github-link",
        ),
    ],
)

