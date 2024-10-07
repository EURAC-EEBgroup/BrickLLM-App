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
        dmc.Paper(
            children = [
                dmc.Text("PROMPTING", c="grey", opacity=0.7, fw=700),
                dmc.Title("Write text to generate brick ontology", lh=1.2, order=3, mt="xs", fw=900, c="black"),
                dmc.Divider(variant = "solid", size="lg", mt=20, color="grey", pt=20, pl=20, pr=20),
                # html.Button("Add Filter", id="add-filter-btn"),
                html.Div(id="test"),
                dmc.ScrollArea(
                    w='100%',
                    children = [
                        html.Div(id="ontology-container-div", children=[]),
                        html.Div(
                            children=[
                                html.Div(id="log-output", style={"whiteSpace": "pre-line"}),
                                dcc.Interval(
                                    id='log-output-interval',
                                    interval=1000,  # in milliseconds
                                    n_intervals=0  # initial number of intervals
                                )
                            ],
                            className='live-log-output'
                        ),
                        dmc.Flex(
                            id="prompt_flex",
                            children = [
                                # dmc.ActionIcon(
                                #     DashIconify(icon="hugeicons:attachment-square", width=70, color="grey"),
                                #     size="lg",
                                #     variant="transparent",
                                #     id="action-icon",
                                #     n_clicks=0,
                                #     style = {'marginTop':'auto', 'bottom':'0'},
                                #     # mb=10,
                                # ),
                                dmc.Textarea(id="prompt_command_ontology", value = prompt_text_example, autosize=True, w="100%",radius="lg", p="md"),
                                dmc.ActionIcon(
                                    DashIconify(icon="solar:send-square-bold", width=100, rotate=1, color="black"),
                                    size="xl",
                                    variant="transparent",
                                    id="btn_icon_ontology",
                                    n_clicks=0,
                                    style = {'marginTop':'auto', 'bottom':'10'}
                                ),
                                
                            ],
                            w="100%"
                        ),
                        dmc.Title("Live Output", lh=1.2, order=3, mt="xs", fw=900, c="black"),
                        
                        html.Div(id="simulation_run"),
                        dmc.Group(
                            children = [
                                dmc.Button(
                                    id="btn_download_ontology",
                                    children = "DOWNLOAD FILE",
                                    fullWidth=True,
                                    radius="lg",
                                    style = {'backgroundColor':'#e12024'},
                                    mt=10
                                ),
                                dcc.Download(id="download_ttl")
                            ],
                            justify="flex-end"
                        ),
                    ]
                ),
            ],
            p="xl",
            mt= 10,
            mb= 10,
            radius="md",
            style={
                "backgroundColor":'white',
                "display": "flex",
                "flexDirection": "column",
                "justifyContent": "space-between",
                "alignItems": "flex-start",
                "backgroundSize": "cover",
                "backgroundPosition": "center",
            },
        )
    ]
)


def layout():

    return layout_