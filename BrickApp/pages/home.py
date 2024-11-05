import dash
from dash import html, dcc
import  dash_mantine_components as dmc
from dash_iconify import DashIconify
from components.sidebar import Sidebar
from components.sidebar import layout_ as layout_sidebar

dash.register_page(__name__, path='/')

prompt_text_example = '''
I have a building located in Bolzano.
It has 3 floors and each floor has 1 office.
There are 2 rooms in each office and each room has three sensors:
- Temperature sensor;
- Humidity sensor;
- CO sensor.
'''
    
layout_ = html.Div(
    [
        html.Div(id="ontology-container-div",children = []),
        html.Div(
            id="ontology-question-div",
            children = [
                dmc.Center(
                    dmc.Flex(
                        id="query_prompt",
                        direction="column",
                        children = [
                            dmc.Flex(
                                id="prompt_flex",
                                children = [
                                    dcc.Textarea(
                                        id="prompt_command_ontology",  
                                        value = prompt_text_example,
                                        placeholder = "Describe your building, systems, sensors, database, etc.",
                                        contentEditable = True, 
                                    ),
                                    dmc.ActionIcon(
                                        id="btn_icon_ontology",
                                        children = DashIconify(id="icon_run", icon="fa6-solid:trowel-bricks",width=25, rotate=1, color="white", flip="vertical", style = {'backgroundcolor':'black'}),
                                        size="xl",
                                        variant="light",
                                    ),
                                    dmc.ActionIcon(
                                        id="btn_ontology_stop",
                                        children = DashIconify(id="icon_stop",icon="ic:round-stop", width=25, rotate=1, color="white"),
                                        size="xl",
                                        variant="light",
                                        radius="xl",
                                        style = {
                                            'marginTop':'auto', 
                                            'bottom':'10',
                                            "border":"1px solid black",
                                            "color":"black",
                                            "padding": "4px",
                                            "borderRadius": "40px",
                                            "marginRight": "10px",
                                            "marginBottom": "5px",
                                            "backgroundColor": "black"
                                        }
                                    ),
                                ],
                                align="center",
                                style = {
                                    'position':'sticky',
                                    "bottom": "40px",
                                }
                            )
                        ]
                    ),
                ),
                dmc.Drawer(
                    id="drawer-simple",
                    padding="md",                    
                    children = [layout_sidebar]
                ),
            ]
        ),
    ]
)

dynamic_background = html.Iframe(
    id="iframe_background_image",
    src="/assets/world-map.html",
    style={
        "position": "fixed",  # Makes the iframe act as a background
        "top": 0,
        "left": 0,
        "bottom": 0,
        "right": 0,
        "width": "100%",
        "height": "100%",
        "overflow": "hidden",  # Hides both x and y overflow
        "border": "none"  # Removes the border around the iframe
    }
)

overall_layout = dmc.AppShellMain(
    [
        dynamic_background,
        html.Div(
            [
                layout_,
                Sidebar
            ]
        )
    ]
    
),


def layout():

    return overall_layout