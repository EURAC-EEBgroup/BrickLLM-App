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
                dmc.ActionIcon(
                    id="setting",
                    children = DashIconify(icon="clarity:settings-line", width=25),
                    variant="transparent",
                    style = {'color':'#e12024'}, 
                )
            ],
            justify="space-between"
        )
    ]
)