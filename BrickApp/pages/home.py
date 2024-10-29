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
    
            




layout_ = html.Div(
    [
        
        # dcc.Interval(id='interval', interval=50, n_intervals=0, disabled=True),  # Update every 50ms
        html.Div(id="ontology-container-div",children = []),
        # dmc.Container(
            # size="xl",
            # children = dmc.Flex(
            #     id="first-child-wrap",
            #     justify = "flex-end",
            #     direction="column",
            #     children = [
                        
            #     ]
            # )
        # ),
        # dmc.Container(
        #     # size="xl",
        #     children = [
        #         dmc.Flex(
        #             direction="column",
        #             w="100%",
        #             mb=10,
        #             children = [
        #                 html.Div(
        #                     id="first-child-wrap",
        #                     children = [
        #                         # dmc.Center(
        #                             html.Div(
        #                                 id="ontology-container-div",
        #                                 children = []
        #                             )
        #                         # )
        #                     ]
        #                 ),
        #             ]
        #         ),
        #     ]
        # ),
        html.Div(
            id="ontology-question-div",
            children = [
                dmc.Center(
                    dmc.Flex(
                        id="query_prompt",
                        direction="column",
                        # style = {
                        #     'marginLeft':"10rem",
                        #     'marginRight':"3rem"
                        # },
                        children = [
                            # html.Div(id='outputS', style={'white-space': 'pre-wrap', 'font-family': 'monospace'}),
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
                                        # className="icon_stop_query",
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
                    # style = {
                    #     "maxWidth":"48rem"
                    # }  
                )
            ]
        )
        
        # dmc.Container(
        #     size = "xl",
            
        #     # children = dmc.Flex(
        #     #     id="query_flex",
        #     #     direction="column",
        #     #     # w="60%",    
        #     children = [
        #         dmc.Flex(
        #             direction="column",
        #             style = {
        #                 'marginLeft':"10rem",
        #                 'marginRight':"3rem"
        #             },
        #             children = [
        #                 dmc.Flex(
        #                     id="prompt_flex",
        #                     children = [
        #                         dcc.Textarea(
        #                             id="prompt_command_ontology",  
        #                             value = prompt_text_example,
        #                             placeholder = "Describe your building, systems, sensors, database, etc.",
        #                             contentEditable = True, 
        #                         ),
        #                         dmc.ActionIcon(
        #                             id="btn_icon_ontology",
        #                             children = DashIconify(id="icon_run", icon="fa6-solid:trowel-bricks",width=25, rotate=1, color="white", flip="vertical", style = {'backgroundcolor':'black'}),
        #                             size="xl",
        #                             variant="light",
        #                         ),
        #                         dmc.ActionIcon(
        #                             id="btn_ontology_stop",
        #                             # className="icon_stop_query",
        #                             children = DashIconify(id="icon_stop",icon="ic:round-stop", width=25, rotate=1, color="white"),
        #                             size="xl",
        #                             variant="light",
        #                             radius="xl",
        #                             style = {
        #                                 'marginTop':'auto', 
        #                                 'bottom':'10',
        #                                 "border":"1px solid black",
        #                                 "color":"black",
        #                                 "padding": "4px",
        #                                 "borderRadius": "40px",
        #                                 "marginRight": "10px",
        #                                 "marginBottom": "5px",
        #                                 "backgroundColor": "black"
        #                             }
        #                         ),
        #                     ],
        #                     align="center",
        #                     style = {
        #                         'position':'sticky',
        #                         "bottom": "40px",
        #                     }
        #                 )
        #             ]
        #         )     
        #     ]
        #     # ),
        #     # mb=5,
        # )
    ]
)

overall_layout =html.Div(
    [
        layout_,
        Sidebar
    ]
)

def layout():

    return overall_layout