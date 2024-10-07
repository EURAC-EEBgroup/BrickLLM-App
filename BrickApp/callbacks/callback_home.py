from dash import Output, Input, State, ctx, callback, dcc,  ALL, Patch, MATCH, no_update
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

@callback(
    Output("btn_icon_ontology","disabled"),
    Input("btn_icon_ontology","n_clicks"),
)
def disable_simulate_btn(btn):
    if btn is None: 
        raise PreventUpdate
    
    disabled = True
    return disabled


@callback(
    Output("simulation_run","children"),
    Output("btn_icon_ontology","disabled", allow_duplicate=True),
    Output("ttl-result", "data"),
    Input("btn_icon_ontology","n_clicks"),
    State("prompt_command_ontology","value"),
    prevent_initial_call=True
)
def run_ontology(btn, text_prompt):
    '''
    Run brickllm library to create ontology form prompt
    '''

    if btn is None: 
        raise PreventUpdate
    
    if ctx.triggered_id == "btn_icon_ontology":
        
        result = True
        simulate_btn_disabled = False
        try:
            log_buffer.seek(0)
            log_buffer.truncate()
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
                with open(f'files/brick_{btn}.ttl', 'w') as f:
                    f.write(ttl_output)

        except Exception as e:
            msg = str(e)
            msg = msg + '-----' + str(os.getcwd())
            print(msg)
            result = False

        finally:
            sys.stdout = sys.__stdout__
            return "", simulate_btn_disabled, result
        
    raise PreventUpdate


@callback(
    Output({"type": "btn_attachment", "index": ALL}, "disabled"),
    Input("ttl-result", "data"),
    State({"type": "btn_attachment", "index": ALL}, "id"),
)
def enable_ttl_download_btn(data, ids):
    if data is None:
        raise PreventUpdate
    
    btns = [no_update] * len(ids)
    if data: 
        btns[-1]=False
    return btns 


@callback(
    Output("log-output-store", "data"),
    Input("log-output-interval", "n_intervals"),
    Input('btn_icon_ontology', 'n_clicks'),
)
def update_logs_store(n, btn):
    if btn is None: 
        raise PreventUpdate

    log_buffer.seek(0)
    logs = log_buffer.read()
    
    return logs


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
                                    )
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
    Output("download_ttl", "data"),
    Input({"type": "btn_attachment", "index": ALL}, "n_clicks"),
    prevent_initial_call=True
)
def test(n_clicks):
    
    if not ctx.triggered:
        raise PreventUpdate
        # return "No button has been clicked yet."
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        button_id = eval(button_id)  # Convert string dictionary representation to dictionary
        print(button_id)
        button_name = f"btn_{button_id['index']}"
        if n_clicks[button_id['index'] - 1] > 0:  # Check if the button has been clicked
            if button_id['type']=="btn_attachment":
                return dcc.send_file(os.getcwd()+f"/BrickApp/files/brick_{button_id['index']}.ttl")
        raise PreventUpdate
        


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


# ==========================================================================================
#                                   DOWNLOAD FILE
# ==========================================================================================

# @callback(
#     Output("download_ttl", "data"),
#     Input("btn_download_ontology", "n_clicks"),
#     prevent_initial_call=True,
# )
# def func(n_clicks):
#     return dcc.send_file(os.getcwd()+"/files/output.ttl")