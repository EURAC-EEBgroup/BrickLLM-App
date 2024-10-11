import dash
from dash import html, dcc
import  dash_mantine_components as dmc
from dash_iconify import DashIconify


dash.register_page(__name__, path='/test')

layout_ = html.Div(
    children = [
        html.Div(
            id='first-child-wrap',
            children=[
                html.Div(
                id='first-child',
                children=[],
            ), 
            ]
        ),
        html.Div(
            id='second-child',
            children=[
                dmc.Textarea(
                    """
                    I have a building located in Bolzano.
                    It has 3 floors and each floor has 1 office.
                    """,
                    autosize=True
                ),
                dmc.Button(
                    "Add card",
                    id='btn_add_card',
                )
            ]
        )
            
    ]
)


def layout():

    return layout_