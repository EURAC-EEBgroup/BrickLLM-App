from dash import Output, Input, State, ctx, callback, dcc,  ALL, Patch, MATCH, no_update, set_props
from dash.exceptions import PreventUpdate
import io
from brickllm.graphs import BrickSchemaGraph
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



@callback(
    Output("simulation_run","children"),
    Output("ttl-result", "data"),
    Input("btn_icon_ontology","n_clicks"),
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
def run_ontology(btn, text_prompt, ttl_result):
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

            # Create an instance of BrickSchemaGraph
            brick_graph = BrickSchemaGraph()

            # Run the graph without streaming
            result = brick_graph.run(
                prompt=text_prompt,
                stream=False
            )

            print(result)
            print(result.get('elem_hierarchy', None))

            ttl_output = result.get('ttl_output', None)

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
            return "", ttl_result
        
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
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify
def text_element_with_file(input_request:str, btn_name_ttl:str, n_clicks):
    component = html.Div(
        children = [
            dmc.ScrollArea( 
                type="hover",       
                h=250,w='100%',
                children = [
                    dmc.Paper(
                        children = [
                            dmc.Stack(
                                children = [
                                    input_request,
                                    dmc.Text(
                                        id='log_output_text',
                                        mt=5,
                                        mb=5,
                                        style={'whiteSpace': 'pre-line'}
                                    ),
                                    dcc.Interval(
                                        id='log-output-interval',
                                        interval=1000,  # in milliseconds
                                        n_intervals=0  # initial number of intervals
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
                                ],
                                align="flex-start"
                            )
                        ],
                        shadow="lg",
                        radius="lg",
                        p="lg",
                        c="red",                
                    )
                ]
            ),
           

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
