import dash
from dash import html, dcc
import  dash_mantine_components as dmc
from dash_iconify import DashIconify


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
                         dmc.Text("In settings, provide the API key of the LLM to be used for generating the ontological model using the Brick schema). If a local model is selected, the API key is not necessary."),
                        #  dmc.Text("If a local model is selected, the API key is not necessary.")
                         ],
                        #  grow=True, 
                        #  justify="flex-start"
                         ),
                    title=dmc.Title("API-KEY required!", order=4, fw=700),
                    variant="filled",
                    color="yellow",
                    radius="lg",
                    mb=10
                ),
                dmc.Text("PROMPTING",id="text1", opacity=0.7, fw=700),
                dmc.Title("Write text to generate brick ontology", id="text2",lh=1.2, order=3, mt="xs", fw=900),
                dmc.Divider(variant = "solid", size="lg", mt=20, color="grey", pt=20, pl=20, pr=20),
                # html.Div(id="ontology-container-div", children=[]),
            ],
            style={
                "position": "relative",
                "z-index": 1000,  # Ensures this content appears above the background
                "color": "white"  # Example styling
            }
        ),
        dmc.Flex(
            direction="column",
            children = [
                dmc.Flex(
                    direction = "column",
                    id="ontology-container-div", children=[], 
                    style = {
                        'overflow':'hidden'
                    }
                    # style = {
                    #     # "height": "calc(100vh - 100px)",
                    #         # 'position':'absolute',
                    #         # "top": "0",
                    #         # "left": "0",
                    #         # "right": "0",
                    #         # "bottom": "0",
                    #         # "overflow-y": "scroll",
                    #     }
                ),
                dmc.Flex(
                    id="prompt_flex",
                    children = [
                        dmc.Textarea(
                            id="prompt_command_ontology", 
                            value = prompt_text_example, 
                            autosize=True, 
                            w="100%",
                            style = {
                                'backgroundColor':'transparent',
                                'color': 'black',
                                'fontSize': '18px',
                                'border': '0px'
                            }),
                        dmc.ActionIcon(
                            id="btn_icon_ontology",
                            children = DashIconify(id="icon_run", icon="fa6-solid:trowel-bricks",width=25, rotate=0, color="black", flip="horizontal"),
                            size="xl",
                            variant="transparent",
                            style = {
                                'marginTop':'auto', 
                                'bottom':'20',
                                'border':'2px solid black',
                                'color':'black',
                                'padding':'2px',
                                'borderRadius':'40px',
                                'marginRight':'2px',
                                'marginBottom':'2px'}
                        ),
                        dmc.ActionIcon(
                            DashIconify(icon="fluent:record-stop-24-regular", width=100, rotate=1, color="black"),
                            size="xl",
                            variant="transparent",
                            id="btn_ontology_stop",
                            style = {'marginTop':'auto', 'bottom':'10'}
                        ),
                        html.Div(id='scroll-trigger', style={'display': 'none'}),
                        
                    ],
                    # w="100%",
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



def layout():

    return layout_