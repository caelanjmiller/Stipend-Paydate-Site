import dash_bootstrap_components as dbc
from dash import html

money_icon = html.I(className="fa-solid fa-sack-dollar fa-fw")

date_query_button = dbc.Row(
    className="query-height justify-content-center align-items-center",
    children=[
        dbc.Col(
            children=[
                dbc.Button(
                    "Click For Next Pay Date",
                    color="primary",
                    className="d-grid gap-2 mx-auto",
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
        html.Div(
            children=[
                html.A(
                    children=[
                        "Caelan Miller",
                        html.I(
                            className="fa-brands fa-github fa-fw",
                            style={"margin": "auto"},
                        ),
                    ],
                    target="_blank",
                    href="https://github.com/caelanjmiller",
                    id="github-link",
                )
            ],
        ),
    ],
)

site_nav = dbc.NavbarSimple(
    id="navbar",
    children=[
        dbc.NavItem(dbc.NavLink("About", href="/about")),
    ],
    brand="When Am I Getting Paid?",
    color="primary",
    dark=True,
)
