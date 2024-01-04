import dash_bootstrap_components as dbc
from dash import html

money_sack_icon = html.I(className="fa-solid fa-sack-dollar fa-fw")
dollar_icon = html.I(className="fa-solid fa-dollar-sign", style={"margin": ".15rem"})
calendar_icon = html.I(className="fa-solid fa-calendar fa-fw")
email_icon = html.I(className="fa-solid fa-inbox fa-fw")

download_calendar_button = dbc.Col(
    children=[
        dbc.Button(
            color="dark",
            id="download-btn",
            children=[
                "Download Calendar",
                calendar_icon,
            ],
        ),
    ]
)

date_query_button = dbc.Row(
    className="query-height justify-content-center align-items-center",
    children=[
        dbc.Col(
            children=[
                dbc.Button(
                    children=[dollar_icon, dollar_icon, dollar_icon],
                    color="dark",
                    id="date-btn",
                ),
            ]
        )
    ],
)

github_calling_card = html.Div(
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
)

page_footer = dbc.Row(
    className="bg-dark justify-content-center align-items-center",
    id="page-footer",
    children=[github_calling_card],
)

site_nav = dbc.NavbarSimple(
    id="navbar",
    className="navbar-dark fixed-top bg-dark",
    children=[
        dbc.NavItem(
            dbc.NavLink(
                "Home",
                href="/",
                external_link=True,
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "About",
                href="/about",
                id="about-link",
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Repo",
                href="https://github.com/caelanjmiller/Stipend-Paydate-Site",
                external_link=True,
            )
        ),
    ],
    fixed=True,
    fluid=True,
    brand="When Am I Getting Paid?",
    brand_href="/",
    brand_external_link=True,
    dark=True,
)

site_jumbotron = dbc.Container(
    className="jumbotron",
    children=[
        html.Div(
            children=[
                html.H4("📅💰 Want to Know When Your Next Stipend Check Is?"),
                html.P(
                    "Click to Find Out Next Pay Date and Download Calendar for Schedule"
                ),
            ]
        )
    ],
)


contact_info = html.Div(
    children=[email_icon, html.A("Email me", href="mailto: caelanjmiller@wustl.edu")]
)

about_page_content = dbc.Row(
    children=[
        dbc.Col(
            children=[
                html.H2("About this Site", style={"text-align": "center"}),
                html.P(
                    "Hi I am Caelan Miller and a first year PhD student in the WUSTL DBBS Computational & Systems Biology Program. I was tired of having to check the WUSTL Finance website for pay dates and having to manually add dates to my calendar. I definitely spent more time coding this site but I chose to create it as both an exercise for myself and a resource for other DBBS PhD students!"
                ),
            ]
        ),
        dbc.Col(
            children=[
                html.Div(
                    children=[html.H2("Questions, Bugs, or Comments?"), contact_info],
                    style={"text-align": "center"},
                ),
            ]
        ),
    ]
)
