import dash
from dash import html, dcc
import  dash_mantine_components as dmc
from dash_iconify import DashIconify
from components.sidebar import Sidebar

dash.register_page(__name__, path='/')

prompt_text_example = '''
I have a building located in Bolzano.
It has 3 floors and each floor has 1 office.
There are 2 rooms in each office and each room has three sensors:
- Temperature sensor;
- Humidity sensor;
- CO sensor.
'''
    
            




layout_ = dmc.Container(
    children = [
        html.Iframe(
            id="iframe_background_image",
            src="/assets/world-map.html",
            style={
                "position": "fixed",  # Makes the iframe act as a background
                "top": 0,
                "left": 0,
                "bottom": 0,
                "right": 0,
                "width": "110%",
                "height": "110%",
                "overflow": "hidden",  # Hides both x and y overflow
                "border": "none"  # Removes the border around the iframe
            }
        ),
        html.Div(
            children=[
                dmc.Alert(
                    id="alert_api_key",
                    children = dmc.Group(
                        [
                            # dmc.Text("In settings,"),
                        #  DashIconify(icon="lets-icons:setting-fill",width=20),
                         dmc.Text("Provide the API key of the LLM to be used for generating the ontological model using the Brick schema). If a local model is selected, the API key is not necessary."),
                        #  dmc.Text("If a local model is selected, the API key is not necessary.")
                         ],
                        #  grow=True, 
                        #  justify="flex-start"
                         ),
                    title=dmc.Title("API-KEY required!", order=4, fw=700),
                    variant="filled",
                    # color="yellow",
                    radius="lg",
                    mb=10,
                    style = {'backgroundColor':'#0F4881'}
                ),
                dmc.Text("PROMPTING",id="text1", opacity=0.7, fw=700, c="black"),
                dmc.Title("Write text to generate brick ontology", id="text2",lh=1.2, order=3, mt="xs", fw=900, c="black"),
                dmc.Divider(variant = "solid", size="lg", mt=20, color="grey", pt=20, pl=20, pr=20),
            ],
            style={
                "position": "relative",
                "zIndex": 1000,  # Ensures this content appears above the background
                "color": "white"  # Example styling
            }
        ),
        dmc.Flex(
            direction="column",
            children = [
                html.Div(
                    id="first-child-wrap",
                    children = [
                        html.Div(
                            id="ontology-container-div",
                            children = []
                        ),
                    ]
                ),
                # dmc.Flex(
                #     direction = "column",
                #     id="ontology-container-div", children=[], 
                #     style = {
                #         'overflow':'hidden'
                #     }                    
                # ),
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
                            children = DashIconify(id="icon_run", icon="fa6-solid:trowel-bricks",width=25, rotate=0, color="white", flip="horizontal", style = {'backgroundcolor':'black'}),
                            size="xl",
                            variant="transparent",
                        ),
                        dmc.ActionIcon(
                            DashIconify(icon="fluent:record-stop-24-regular", width=100, rotate=1, color="black", ),
                            size="xl",
                            variant="transparent",
                            id="btn_ontology_stop",
                            style = {'marginTop':'auto', 'bottom':'10'}
                        ),
                    ],
                    align="center",
                    style = {
                        'position':'sticky',
                        # 'zIndex':'999',
                        # "height": "100px",  # Fixed height
                        # "left": "0",
                        # "right": "0",
                        "bottom": "40px",
                        # "top":"auto"
                    }
                )
            ]
        )     
    ]
)

overall_layout =html.Div(
    [layout_,
    Sidebar]
)

def layout():

    return overall_layout