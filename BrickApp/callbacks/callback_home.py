from dash import Output, Input, State, ctx, callback, dcc,  ALL, Patch, MATCH, no_update, set_props, html, clientside_callback, ClientsideFunction, get_relative_path
from dash.exceptions import PreventUpdate
from dash_iconify import DashIconify
import dash_mantine_components as dmc
import dash
from urllib.parse import urlparse

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from brickllm.graphs import BrickSchemaGraph, BrickSchemaGraphLocal


import io
import sys
import os
import time
import random

log_buffer = io.StringIO()

'''

# Specify the user prompt
building_description = """
I have a building located in Bolzano.
It has 3 floors and each floor has 1 office.
There are 2 rooms in each office and each room has three sensors:
- Temperature sensor;
- Humidity sensor;
- CO sensor.
"""

# Create an instance of BrickSchemaGraph
brick_graph = BrickSchemaGraph()

# Display the graph
brick_graph.display()

# Run the graph without streaming
result = brick_graph.run(
    prompt=building_description,
    stream=False
)

print(result)
print(result.get('elem_hierarchy', None))

ttl_output = result.get('ttl_output', None)

# Save the output to a file
if ttl_output:
    print(ttl_output)
    with open('output.ttl', 'w') as f:
        f.write(ttl_output)
'''


# clientside_callback(
#     """
#     function(value) {
#         var textarea = document.getElementById('prompt_command_ontology');
#         textarea.style.height = 'auto';  // Reset height to auto to recalculate
#         textarea.style.height = textarea.scrollHeight + 'px';  // Set height to scrollHeight
#         return value;  // Return the value to keep the callback functional
#     }
#     """,
#     Output('prompt_command_ontology', 'value'),
#     Input('prompt_command_ontology', 'value')
# )


clientside_callback(
    """
    function updateLoadingState(n_clicks) {
        return true
    }
    """,
    Output("loading-overlay", "visible", allow_duplicate=True),
    Input("load-button", "n_clicks"),
    prevent_initial_call=True,
)

 # NOTIFICATION MISSING API
notification_text = dmc.Notification(
        title=dmc.Text("Hey there!",c="red",size="lg"),
        id="simple-notify",
        action="show",
        message=dmc.Text("Provide the API key of the LLM to be used for generating the ontological model using the Brick schema). If a local model is selected, the API key is not necessary.",c="black"),
        icon=DashIconify(icon="iconamoon:attention-circle-duotone", color="white",width=45),
        radius="xl",
        style = {'backgroundColor':'white', 'border':'1px solid #0F4881'},
        closeButtonProps = {'color':'white'},
        w='100%'
    )
@callback(
    Output("notifications-container", "children"),
    Input("btn_confirm_model","checked"),
    State("llm_model_type","value"),
    State("api-key_value","value"),
    prevent_initial_call=True,
)
def show(btn, model_type, api_key):
    if btn :
        if model_type == "llm_model":
            if api_key == None or api_key == "":
                return notification_text

# ======
'''Text Warning time for local model'''
@callback(
    Output("local_warning_time","children"),
    Input("llm_model_type","value")
)
def text_time_warning(model_):
    '''
    Text local warning time if model selection is local. 
    It requires time to generate ttl
    '''
    childrenT = "The generation of the ontology model using LLM may take some time even more than 5 minutes depending on the request. We are working to reduce this problem. We apologize for the inconvenience."
    if model_ == "local_model":        
        child = html.Div(
            [
            dmc.Group(
                [
                    DashIconify(icon="material-symbols:construction", width=30),
                    dmc.Text("UNDER CONSTRUCTION", size="lg", c="rgb(223 27 18)"),
                    
                ]
            ),
            dmc.Divider(variant="solid", color="grey", size="lg"),
            dmc.Text(childrenT, id="warning_class_time", opacity = 0.9, mt=10, style = {'textAlign':'justify'})
            ],
           style = {
                "border":"1px solid grey",
                "border-radius": "20px",
                "transition": "boxShadow 0.3s ease",
                "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.2)",
                "padding": "20px",
                "margin-top": "10px",
            }
        )
        return child
    else:
        return  ""
# ======

# ================================================
#          CHECK API KEY
# ================================================

# ======
''' DISABLED MODEL SELECTION IF LLM LOCAL MODEL HAS CHOSEN'''

@callback(
    Output("llm_model_type","disabled"),
    Output("llm_model_","disabled"),
    Output("llm_model_version","disabled"),
    Output("api-key_value","disabled"),
    Output("llm_model_local_huggin","disabled"),
    Input("btn_confirm_model","checked"),
    State("api-key_value","value"),
)
def block_selection(btn, APikey):
    if btn:
        return True, True, True, True, True
    return False, False, False, False, False, 
    


@callback(
    Output("prompt_command_ontology","disabled"),
    Output("btn_icon_ontology","disabled"),
    Output("prompt_flex","className"),
    Output("btn_icon_ontology","className"),
    Input("btn_confirm_model","checked"),
    State("llm_model_type","value"),
    State("api-key_value","value")
)
def enable_prompt(btn, model_type, api_key):
    '''
    if llm model is selected the api-key should be given 
    '''

    if btn :
        if model_type == "llm_model":
            if api_key == None or api_key == "":
                return True, True,"promtp_flex_disabled", "icon_run_disabled_style"
        elif model_type == "local_model":
            return False, False,"promtp_flex_not_disabled", "icon_run_not_disabled_style"
        return False, False,"promtp_flex_not_disabled", "icon_run_not_disabled_style"
    else:
        return True, True,"promtp_flex_disabled", "icon_run_disabled_style"


# ================================================
#           STYLE:DISSOLVING ICON RUN
# ================================================
'''
if no value in the prompt the run button desappers
'''
style_hide = {
    'marginTop':'auto', 
    'bottom':'20',
    'border':'2px solid black',
    'color':'black',
    'padding':'2px',
    'borderRadius':'40px',
    'marginRight':'2px',
    'marginBottom':'2px', 
    'transition': 'opacity 2s', 
    'opacity': 0
}
style_action_icon_on = {
    'marginTop':'auto', 
    'bottom':'20',
    'border':'2px solid black',
    'color':'black',
    'padding':'2px',
    'borderRadius':'40px',
    'marginRight':'2px',
    'marginBottom':'2px',
    'transition': 'opacity 2s', 
    'opacity': 1
}

@callback(
    Output("btn_icon_ontology",'display'),
    Input("prompt_command_ontology", 'value'),
    State("btn_icon_ontology",'display'),
    prevent_initial_call=True
)
def hide_run_button(valPrompt, stateDisplay):
    if valPrompt and stateDisplay=="none":
        return True
    elif valPrompt.strip()=="" and stateDisplay:
        return "none"
    else: 
        PreventUpdate
    


# ================================================
#           STYLE: NIGHT AND DAY 
# ================================================

# @callback(
#     Output('modalText1',"c"),
#     Output('sidebarText2',"c"),
#     Output('sidebarText3',"c"),
#     Output('sidebarText4',"c"),
#     Output('sidebarText5',"c"),
#     Output('confirmSelection',"c"),
    
#     # Output('title_model_upload',"c"),
#     # Output('iframe_background_image',"src"),
#     Output('logo_header',"src"),
#     Input("mantine-provider", "forceColorScheme"),
#     # prevent_initial_call=True
# )
# def change_color_style(theme):
#     if theme == 'dark':
#         return "white","white","white","white","white","white","/assets/world-map_dark.html", get_relative_path("/assets/eurac_logo_white_WEB_neg.png"),
#     else:
#         return "black", "black","black", "black","black","black","/assets/world-map.html", get_relative_path("/assets/eurac_logo_grey_WEB_pos.png"),
    


# ================================================
#           FAKE FUNCTION for testing 
# ================================================

def dummy_simulation():
    for i in range(30):
        print(f"asdgasdgasg {i}")
        time.sleep(1)
 
    return str(time.time()) + str(random.randint)

# ================================================
#            RUN FUNCTION TO CREATE MODEL 
# ================================================

class BackgroundBuffer:
    """ Take the contents of stdout during a background callback and put it into dcc.Store. """
    def write(self, message):
        if message.strip():
            set_props(
                "log-progress-store",
                {'data': message}
            )
        
    def flush(self):  # Required for compatibility with the standard output
        pass


#"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"
def brick_simulation(text_prompt, api_key_client, model_GPT):
    # Load environment variables
    load_dotenv()
    # Create an instance of BrickSchemaGraph with a custom model
    custom_model = ChatOpenAI(temperature=0, model=model_GPT, api_key=api_key_client)
    brick_graph = BrickSchemaGraph(model=custom_model)

    # Prepare input data
    input_data = {"user_prompt": text_prompt}
    
    # Run the graph without streaming
    result = brick_graph.run(
        input_data=input_data,
        stream=False
    )
    print(result)
    print(result.get('elem_hierarchy', None))

    return result

def brick_simulation_local(building_description, local_model_name):
    # Create an instance of BrickSchemaGraphLocal
    brick_graph_local = BrickSchemaGraphLocal(model=local_model_name)

    # Display the graph structure
    # brick_graph_local.display()
    instructions = """
    Your job is to generate a RDF graph in Turtle format from a description of energy systems and sensors of a building in the following input, using the Brick ontology.
    ### Instructions:
    - Each subject, object of predicate must start with a @prefix.
    - Use the prefix bldg: with IRI <http://my-bldg#> for any created entities.
    - Use the prefix brick: with IRI <https://brickschema.org/schema/Brick#> for any Brick entities and relationships used.
    - Use the prefix unit: with IRI <http://qudt.org/vocab/unit/> and its ontology for any unit of measure defined.
    - When encoding the timeseries ID of the sensor, you must use the following format: ref:hasExternalReference [ a ref:TimeseriesReference ; ref:hasTimeseriesId 'timeseriesID' ].
    - When encoding identifiers or external references, such as building/entities IDs, use the following schema: ref:hasExternalReference [ a ref:ExternalReference ; ref:hasExternalReference ‘id/reference’ ].
    - When encoding numerical reference, use the schema [brick:value 'value' ; \n brick:hasUnit unit:'unit' ] .
    -When encoding coordinates, use the schema brick:coordinates [brick:latitude "lat" ; brick:longitude "long" ].
    The response must be the RDF graph that includes all the @prefix of the ontologies used in the triples. The RDF graph must be created in Turtle format. Do not add any other text or comment to the response.
    """
    # Prepare input data
    input_data = {
        "user_prompt": building_description,
        "instructions": instructions
    }

    # Run the graph
    result = brick_graph_local.run(input_data=input_data, stream=False)

    # Print the result
    print(result)

    # Save the result to a file
    return result
    # brick_graph_local.save_ttl_output("my_building_local.ttl")

@callback(
    # Output("simulation_run","children"),
    Output("ttl-result", "data"),
    Input("btn_icon_ontology","n_clicks"),
    State("prompt_command_ontology","value"),
    State("ttl-result", "data"),
    State("api-key_value","value"),
    State("llm_model_version","value"),
    State("llm_model_type","value"),
    State("llm_model_local_huggin","value"),
    background=True,
    running=[
        (Output("btn_icon_ontology", "display"), "none", True),
        (Output("btn_ontology_stop", "display"), True, "none"),
    ],
    cancel=[
        Input('btn_ontology_stop', 'n_clicks')
    ],
    prevent_initial_call=True
)
def run_ontology(btn, text_prompt, ttl_result, apiKey, GPTtype,ll_model_type, local_model_name):
    '''
    Run brickllm library to create ontology form prompt
    '''

    if btn is None: 
        raise PreventUpdate
    
    ttl_result[f"brick_{btn}.ttl"] = None

    if ctx.triggered_id == "btn_icon_ontology":
        
        try:
            log_buffer = BackgroundBuffer()
            sys.stdout = log_buffer

            if ll_model_type == "llm_model":
            # ============================================
                # 1. Case LLM 
                result = brick_simulation(text_prompt=text_prompt, api_key_client=apiKey, model_GPT=GPTtype)
                ttl_output = result.get('ttl_output', None)
                # ttl_output = dummy_simulation()
                # Save the output to a file
                if ttl_output:
                    print(ttl_output)
                    ttl_result[f"brick_{btn}.ttl"] = ttl_output

            else:   
                raise Exception ("Local LLM not available yet")       
                # # ============================================
                # # 2. Case Local LLM
                # brick_graph_local = brick_simulation_local(text_prompt, local_model_name)
                # if brick_graph_local:
                #     ttl_result[f"brick_{btn}.ttl"] = brick_graph_local


        except Exception as e:
            msg = str(e)
            msg = msg + '-----' + str(os.getcwd())
            print(msg)

        finally:
            sys.stdout = sys.__stdout__
            return ttl_result
        
    raise PreventUpdate


@callback(
    Output({"type": "btn_attachment", "index": ALL}, "disabled"),
    Input("ttl-result", "data"),
    State({"type": "btn_attachment", "index": ALL}, "id"),
)
def enable_ttl_download_btn(data, ids):
    if data == {}:
        raise PreventUpdate
    
    btns = [no_update] * len(ids)

    filename = f"brick_{(len(ids))}.ttl"
    if filename in data and data[filename]: 
        btns[0]=False # update only last button

    return btns 


@callback(
    Output("log-output-store", "data"),
    Input("log-progress-store", "data"),
    State("log-output-store", "data"),
)
def update_logs_store(progress_data, output_data):
    if progress_data == '': 
        raise PreventUpdate
    
    logs = output_data + '\n' + progress_data
    
    return logs


@callback(
    Output("log-output-store", "data", allow_duplicate=True),
    Input("btn_icon_ontology","n_clicks"),
    prevent_initial_call=True
)
def clear_old_logs(btn):
    if btn is None: 
        raise PreventUpdate
    
    return ""



# import time
# def print_text_animation(text):
#     for char in text:
#         print(char, end="", flush=True)
#         time.sl


# @callback(
#     # Output('outputS', 'children'),
#     Output({'type':"log_output_text", 'index':MATCH}, "children"),
#     Output({'type':'log-output-interval', 'index':MATCH}, 'n_intervals'),
#     Input({'type':'log-output-interval', 'index':MATCH}, 'n_intervals'),
#     # Output("interval", 'n_intervals'),
#     # Input("interval", 'n_intervals'),
#     Input("log-output-store", "data"),
#     # State('outputS', 'children')
#     State({'type':"log_output_text", 'index':MATCH}, "children")
# )
# def update_logs(n_intervals,text, current_output):
#     if n_intervals == 0:
#         return "", 0  # Initial state

#     # Initialize current_output if None
#     if current_output is None:
#         current_output = ""

#     # Reveal more characters for each interval
#     if len(current_output) < len(text):
#         # Adjust the number of characters revealed at each interval
#         characters_to_reveal = min(1, len(text) - len(current_output))
#         new_output = current_output + text[len(current_output):len(current_output) + characters_to_reveal]
#         return new_output, n_intervals + 1  # Increment intervals
#     else:
#         return current_output, n_intervals  # Stop updating when complete


@callback(
    Output({'type':"log_output_text", 'index':ALL}, "children"),
    Input("log-output-store", "data"),
    State({'type':"log_output_text", 'index':ALL}, "id"),
)
def update_logs(data, ids):
    if ids == []: 
        raise PreventUpdate
    
    children = [dash.no_update] * len(ids)
    children[0] = data
    
    return children



# @callback(
#     Output("log_output_text", "children"),
#     [Input("log-output-interval", "n_intervals")],
#     [State("log-output-store", "data"),
#      State("log_output_text", "children")]
# )
# def update_logs(n_intervals, data, current_text):
#     if not data:
#         raise PreventUpdate
    
#     # Check if all text has been displayed
#     if current_text is None:
#         current_text = ""

#     # Determine how many characters to display
#     length = len(current_text)
    
# #     if length >= len(data):
# #         raise PreventUpdate  # Stop updating if all text is displayed

#     # Add the next character
#     next_character = data[length]  # Get the next character to display
#     return current_text + next_character

# ==========================================================================================
#                                   APPEND EACH REQUEST 
# ==========================================================================================

def text_element_with_file(input_request:str, btn_name_ttl:str, n_clicks, index):
    component = dmc.Center(
        id={"type": "card", "index": index},
        style = {
            'zIndex':'1',
            'width':"100%",
            'maxWidth':'100%'
            # 'marginLeft':'auto',
            # 'marginRight':'2rem',
            },
        children = [
            dmc.Flex(
                id="card_query_response",
                direction="column",
                children = [
                    dmc.Flex(
                        children = [
                            dmc.ThemeIcon(
                                children = DashIconify(icon="fluent-color:chat-bubbles-question-16", width=45),
                                radius = "lg",
                                variant= "outline",
                                color="black",
                                style = {
                                    'border':"0px",
                                    # 'border':"1px solid lightgrey",
                                    # "transition": "boxShadow 0.3s ease",
                                    # "boxShadow": "0px 4px 6px rgba(0, 0, 0, 0.2)",

                                    },
                                size="lg"
                            ),
                            dmc.Paper(
                                id="text_prompt_question",
                                children = [
                                    input_request,
                                ],
                                shadow="lg",
                                radius="lg",
                                p="lg",
                                style = {'fontSize':'1rem'}
                            ),
                        ],
                        gap={"base": "sm", "sm": "lg"},
                    ),
                    dmc.Spoiler(
                        showLabel="Show more",
                        hideLabel="Hide",
                        maxHeight=100,
                        expanded = True,
                        # mb=10,
                        children=[
                            dmc.Stack(
                                children = [
                                    dmc.ScrollArea(
                                        children = [
                                            dmc.Text(
                                                id={'type':'log_output_text', 'index':index},
                                                mt=5,
                                                mb=5,
                                                c="black",
                                                style={'whiteSpace': 'pre-line','fontSize':'1rem'}
                                            ),
                                        ],
                                        type="hover"
                                    ),
                                    dmc.Button(
                                        id={"type": "btn_attachment", "index": n_clicks},
                                        children = dmc.Text(f"{btn_name_ttl}.ttl", td="underline"),
                                        leftSection= DashIconify(icon="hugeicons:attachment-square", width=20, color="grey"),
                                        variant="transparent",
                                        n_clicks=0,
                                        disabled=True,
                                    ),
                                    dcc.Download(id={"type": "download_ttl", "index": n_clicks})

                                    
                                ],
                            )
                        ],
                        style = {
                            "backgroundColor": "white",
                            "borderRadius": "20px",
                            "marginTop": "10px",
                            "padding": "20px",
                            "boxShadow": "0 8px 16px rgba(0, 0, 0, 0.2)",
                            "marginLeft": "5px"
                            }
                    )
                ],            
            )
        ]
    )
    return component





@callback(
    Output("ontology-container-div", "children"),
    Input("btn_icon_ontology", "n_clicks"),
    State("prompt_command_ontology","value"),
)
def display_dropdowns(btn_clicks, prompt_text):
    if btn_clicks is None: 
        raise PreventUpdate

    index = btn_clicks    
    patched_children = Patch()
    text_to_append = text_element_with_file(prompt_text, f"brick_{btn_clicks}", btn_clicks, index)
    patched_children.insert(0,text_to_append)

    return patched_children
    
#                                   SAVE TTL FILE AND MAKE AVAILABLE 
# ==========================================================================================

@callback(
    Output({"type": "download_ttl", "index": MATCH}, "data"),
    Input({"type": "btn_attachment", "index": MATCH}, "n_clicks"),
    State("ttl-result", "data"),
    prevent_initial_call=True
)
def test(n_clicks, ttl_data):
    if not n_clicks: 
        raise PreventUpdate
    
    filename = f"brick_{ctx.triggered_id['index']}.ttl"
    data = ttl_data[filename]
    return dcc.send_string(data, filename)
        


@callback(
    Output({"type": "btn_attachment", "index": ALL}, "n_clicks"),
    Input("btn_icon_ontology", "n_clicks"),
    State({"type": "btn_attachment", "index": ALL}, "id"),
)
def update_buttons_state(btn, ids):
    """ Workaround to keep ttl download buttons not active on btn_icon_ontology click"""
    if btn is None: 
        raise PreventUpdate

    btns = [0] * len(ids)
    return btns


@callback(
    Output("drawer-simple", "opened"),
    Input("burger_mobile", "n_clicks"),
    State("drawer-simple", "opened")
)
def toggle_drawer(n_clicks, is_opened):
    if n_clicks:
        return not is_opened  # Toggle the state of the drawer
    return is_opened  # Return the current state if no clicks yet



