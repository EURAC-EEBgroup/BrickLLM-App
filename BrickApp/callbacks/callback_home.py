from dash import Output, Input, State, ctx, callback, dcc,  ALL, Patch, MATCH, no_update, set_props, html, get_relative_path, clientside_callback
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

clientside_callback(
    """
    function(n_clicks) {
        var mainDiv = document.getElementById('ontology-container-div');
        if (mainDiv) {
            mainDiv.scrollTop = mainDiv.scrollHeight;
        }
        return '';
    }
    """,
    Output('scroll-trigger', 'children'),
    Input('btn_icon_ontology', 'n_clicks'),
)

# ================================================
#          CHECK API KEY
# ================================================

@callback(
    Output("prompt_command_ontology","disabled"),
    Output("alert_api_key","hide"),
    Input("llm_model_type","value"),
    Input("api-key_value","value")
)
def enable_prompt(model_type, api_key):
    '''
    if llm model is selected the api-key should be given 
    '''

    if model_type == "llm_model":
        if api_key == None or api_key == "":
            return True, False
    elif model_type == "local_model":
        return False, True
    return False, True





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
    raise PreventUpdate
    


# ================================================
#           STYLE: NIGHT AND DAY 
# ================================================

@callback(
    Output('text1',"c"),
    Output('text2',"c"),
    # Output('modalText1',"c"),
    # Output('modalText2',"c"),
    # Output('llm_model_',"c"),
    # Output('title_model_upload',"c"),
    Output('iframe_background_image',"src"),
    Output('logo_header',"src"),
    Input("mantine-provider", "forceColorScheme"),
    # prevent_initial_call=True
)
def change_color_style(theme):
    if theme == 'dark':
        return "red", "white", "/assets/world-map_dark.html", get_relative_path("/assets/eurac_logo_white_WEB_neg.png"),
    else:
        return "grey", "black", "/assets/world-map.html", get_relative_path("/assets/eurac_logo_grey_WEB_pos.png"),
    


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
    Input("api-key_value","value"),
    Input("llm_model_version","value"),
    State("prompt_command_ontology","value"),
    State("ttl-result", "data"),
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
def run_ontology(btn, apiKey, GPTtype, text_prompt, ttl_result):
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
    Output("log_output_text", "children"),
    Input("log-output-store", "data"),
)
def update_logs(data):

    return data


# ==========================================================================================
#                                   APPEND EACH REQUEST 
# ==========================================================================================

def text_element_with_file(input_request:str, btn_name_ttl:str, n_clicks):
    component = html.Div(
        children = [
            dmc.ScrollArea( 
                type="hover",       
                h=250,w='100%',
                children = [
                    dmc.Paper(
                        children = [
                            input_request,
                        ],
                        shadow="lg",
                        radius="lg",
                        p="lg",
                        c="red",
                        ml=150
                    ),
                    dmc.Spoiler(
                        showLabel="Show more",
                        hideLabel="Hide",
                        maxHeight=100,
                        children=[
                            dmc.Stack(
                                children = [
                                    dmc.Text(
                                        id='log_output_text',
                                        mt=5,
                                        mb=5,
                                        c="red",
                                        style={'whiteSpace': 'pre-line'}
                                    ),
                                    dcc.Interval(
                                        id='log-output-interval',
                                        interval=1000,  # in milliseconds
                                        n_intervals=0  # initial number of intervals
                                    ),
                                    
                                ],
                                align="flex-start"
                            )
                        ],
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
                ]
            )
        ]
    )
    

    return component


@callback(
    Output("ontology-container-div", "children"),
    Input("btn_icon_ontology", "n_clicks"),
    # Input("log-output-interval", "n_intervals"),
    State("prompt_command_ontology","value"),
    # prevent_initial_call=True
)
def display_dropdowns(n_clicks, prompt_text):
    patched_children = Patch()
    if ctx.triggered_id == "btn_icon_ontology":
        text_to_append = text_element_with_file(prompt_text, f"brick_{n_clicks}", n_clicks)
        patched_children.append(text_to_append)

        # patched_children_logs = Patch()       
        # log_buffer.seek(0)
        # logs = log_buffer.read()
        # logs_paper = dmc.Paper(
        #     children = logs,
        #     shadow="lg",
        #     radius="lg",
        #     p="lg",
        #     mt=10,
        #     c="green",
        #     h=200
        # )
        # patched_children.append(logs_paper)
        return patched_children
    raise PreventUpdate


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
