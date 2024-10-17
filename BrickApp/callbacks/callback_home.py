from dash import Output, Input, State, ctx, callback, dcc,  ALL, Patch, MATCH, no_update, set_props, html, clientside_callback, ClientsideFunction, get_relative_path
from dash.exceptions import PreventUpdate
from dash_iconify import DashIconify
import dash_mantine_components as dmc

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from brickllm.graphs import BrickSchemaGraph

import io
import sys
import os

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
#     function(n_clicks) {
#         var mainDiv = document.getElementById('ontology-container-div');
#         if (mainDiv) {
#             mainDiv.scrollTop = mainDiv.scrollHeight;
#         }
#         return '';
#     }
#     """,
#     Output('scroll-trigger', 'children'),
#     Input('btn_icon_ontology', 'n_clicks'),
# )
clientside_callback(
    """
    function(value) {
        var textarea = document.getElementById('prompt_command_ontology');
        textarea.style.height = 'auto';  // Reset height to auto to recalculate
        textarea.style.height = textarea.scrollHeight + 'px';  // Set height to scrollHeight
        return value;  // Return the value to keep the callback functional
    }
    """,
    Output('prompt_command_ontology', 'value'),
    Input('prompt_command_ontology', 'value')
)


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

# ================================================
#          CHECK API KEY
# ================================================
@callback(
    Output("llm_model_type","disabled"),
    Output("llm_model_","disabled"),
    Output("llm_model_version","disabled"),
    Output("api-key_value","disabled"),
    Input("btn_confirm_model","checked"),
    State("llm_model_type","value"),
)
def block_selection(btn, model_selection):
    if btn:
    # if ctx.triggered_id == "btn_confirm_model":
        if model_selection == "llm_model":
            return True, True, True, True
        return False, False, False, False
    return False, False, False, False


@callback(
    Output("prompt_command_ontology","disabled"),
    Output("alert_api_key","hide"),
    Output("btn_icon_ontology","disabled"),
    # Output("prompt_command_ontology","style"),
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
    # style_disabled ={'backgroundColor':'#A9A9A9'}
    # style_not_disabled ={'backgroundColor':'#eeeeee'}
    if btn :
        if model_type == "llm_model":
            if api_key == None or api_key == "":
                return True, False, True,"promtp_flex_disabled", "icon_run_disabled_style"
        elif model_type == "local_model":
            return False, True, False,"promtp_flex_not_disabled", "icon_run_not_disabled_style"
        return False, True, False,"promtp_flex_not_disabled", "icon_run_not_disabled_style"
    else:
        return True, False, True,"promtp_flex_disabled", "icon_run_disabled_style"


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

# @callback(
#     Output("btn_icon_ontology",'style'),
#     Input("prompt_command_ontology", 'value'),
#     prevent_initial_call=True
# )
# def hide_run_button(valPrompt):
#     if valPrompt:
#         return style_action_icon_on
#     else:
#         return style_hide

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
import time
import random
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

    # Run the graph without streaming
    result = brick_graph.run(
        prompt=text_prompt,
        stream=False
    )
    print(result)
    print(result.get('elem_hierarchy', None))

    return result

@callback(
    # Output("simulation_run","children"),
    Output("ttl-result", "data"),
    Input("btn_icon_ontology","n_clicks"),
    State("prompt_command_ontology","value"),
    State("ttl-result", "data"),
    State("api-key_value","value"),
    State("llm_model_version","value"),
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
def run_ontology(btn, text_prompt, ttl_result, apiKey, GPTtype,):
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

            
            result = brick_simulation(text_prompt=text_prompt, api_key_client=apiKey, model_GPT=GPTtype)

            ttl_output = result.get('ttl_output', None)
            # ttl_output = dummy_simulation()
 
 
            # Save the output to a file
            if ttl_output:
                print(ttl_output)
                ttl_result[f"brick_{btn}.ttl"] = ttl_output

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
        btns[-1]=False # update only last button

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



@callback(
    # Output("log_output_text", "children"),
    Output({'type':"log_output_text", 'index':MATCH}, "children"),
    Input("log-output-store", "data"),
    # Input('log-output-interval', 'n_intervals')
)
def update_logs(data):
    return data
    # return displayed_text

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
    component = html.Div(
        id={"type": "card", "index": index},
        children = [
            dmc.ScrollArea( 
                type="never",       
                h=250,w='100%',
                children = [
                    dmc.Flex(
                        children = [
                            dmc.ThemeIcon(
                                children = DashIconify(icon="humbleicons:user-asking", width=45),
                                radius = "lg",
                                variant= "outline",
                                color="black",
                                style = {'border':"1px solid lightgrey"},
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
                            ),
                        ],
                        gap={"base": "sm", "sm": "lg"},
                    ),
                    dmc.Spoiler(
                        showLabel="Show more",
                        hideLabel="Hide",
                        maxHeight=100,
                        children=[
                            dmc.Stack(
                                children = [
                                    dmc.Text(
                                        id={'type':'log_output_text', 'index':index},
                                        # id='log_output_text',
                                        mt=5,
                                        mb=5,
                                        c="black",
                                        style={'whiteSpace': 'pre-line'}
                                    ),
                                    dmc.Button(
                                        id={"type": "btn_attachment", "index": n_clicks},
                                        children = dmc.Text(f"{btn_name_ttl}.ttl", td="underline"),
                                        leftSection= DashIconify(icon="hugeicons:attachment-square", width=20, color="grey"),
                                        variant="transparent",
                                        n_clicks=0,
                                        disabled=True
                                    ),
                                    dcc.Download(id={"type": "download_ttl", "index": n_clicks})
                                    # dcc.Interval(id='log-output-interval-text', interval=100, n_intervals=0),
                                    # dcc.Interval(
                                    #     id='log-output-interval',
                                    #     interval=100,  # in milliseconds
                                    #     n_intervals=0  # initial number of intervals
                                    # ),
                                    
                                ],
                                align="flex-start"
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
                    ),
                    
                ]
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

# @callback(
#     Output("sidebar_","display"),
#     Input("url_app","href")
# )
# def visualize_sidebar(href):
#     if href == "http://127.0.0.1:8097/contact":
#         return "none"
#     return True
