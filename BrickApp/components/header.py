import dash_mantine_components as dmc
from dash import get_relative_path,dcc
from dash_iconify import DashIconify

Header = dmc.AppShellHeader(
    id="header_app",
    h=80,
    p=20,
children = [
        
        dmc.Group(
            children = [
                dcc.Link(
                    id="link_eurac5",
                    children = [
                        dmc.Anchor(
                            href = "www.eurac.edu",
                            children = [
                                dmc.Image(
                                    id="logo_header",
                                    h=50,
                                )
                            ]
                        )
                    ],
                    href = "www.eurac.edu",
                ),
                DashIconify(icon="", width=100),
                dmc.ActionIcon(
                    [
                        dmc.Paper(DashIconify(icon="radix-icons:sun", width=25), darkHidden=True),
                        dmc.Paper(DashIconify(icon="radix-icons:moon", width=25), lightHidden=True),
                    ],
                    variant="transparent",
                    color="yellow",
                    id="color-scheme-toggle",
                    size="lg",
                    ms="auto",
                ),
                dmc.Anchor(
                    dmc.ActionIcon(
                        id="github",
                        children = DashIconify(icon="akar-icons:github-fill", width=25),
                        variant="transparent",
                        style = {'color':'#e12024'}, 
                    ),
                    href = "https://github.com/EURAC-EEBgroup/brick-llm/tree/main",
                    target="_blank"
                ),
                dmc.ActionIcon(
                    id="setting",
                    children = DashIconify(icon="lets-icons:setting-fill", width=30),
                    variant="transparent",
                    style = {'color':'#e12024','marginBottom':'5px'}, 
                )
            ],
            justify="space-between"
        )
    ]
)