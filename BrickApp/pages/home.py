import dash
from dash import html, dcc, get_relative_path
import  dash_mantine_components as dmc
from dash_iconify import DashIconify
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
                            # html.Div(id="typewriter-text", style={'fontSize': '24px', 'marginTop': '20px', 'textAlign': 'center'}),
                            dmc.Text(id="typewriter-text", style={'fontSize': '1.5rem', 'marginBottom': '10px', 'textAlign': 'center'}, fw=600),
                            dmc.Flex(
                                id="prompt_flex",
                                children = [
                                    # Div to hold the text with a unique ID
                                    # dcc.Textarea(
                                    #     id="prompt_command_ontology",  
                                    #     value = prompt_text_example,
                                    #     placeholder = "Describe your building, systems, sensors, database, etc.",
                                    #     contentEditable = True, 
                                    #     autosize=True
                                    # ),
                                    dmc.Textarea(
                                        id="prompt_command_ontology",  
                                        value = "",
                                        placeholder = "Describe your building, systems, sensors, database, etc.",
                                        # contentEditable = True, 
                                        autosize=True,
                                        minRows=1,
                                        w="100%"
                                    ),
                                    dmc.ActionIcon(
                                        id="btn_icon_ontology",
                                        children = DashIconify(id="icon_run", icon="fa6-solid:trowel-bricks",width=25, rotate=1, color="white", flip="vertical", style = {'backgroundcolor':'black'}),
                                        size="xl",
                                        variant="light",
                                    ),
                                    dmc.ActionIcon(
                                        id="btn_ontology_stop",
                                        children = DashIconify(id="icon_stop",icon="ic:round-stop",rotate=1, color="white", style = {'width':'2rem'}),
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
                    mt=0,                 
                    position="right",
                    children = [
                        layout_sidebar,    
                    ],
                    style = {'zIndex':1000}
                ),
            ]
        ),
    ],
    style = {"width":"100%"}
)

dynamic_background = html.Iframe(
    id="iframe_background_image",
    src=get_relative_path("/assets/world-map.html"),
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
        # layout_,
        html.Div([layout_,],style = {'justifyItems':'center'})
    ]
),


def layout():

    return overall_layout