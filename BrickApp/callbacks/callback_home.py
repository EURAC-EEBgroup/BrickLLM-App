from dash import Output, Input, State, ctx, callback, dcc,  ALL, Patch, MATCH
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
    Output("simulation_run","children"),
    Input("btn_icon_ontology","n_clicks"),
    State("prompt_command_ontology","value")
)
def run_ontology(btn, text_prompt):
    '''
    Run brickllm library to create ontology form prompt
    '''
    if ctx.triggered_id == "btn_icon_ontology":
        
        result = True
        try:
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
                sys.stdout = sys.__stdout__

        except Exception as e:
            msg = str(e)
            msg = msg + '-----' + str(os.getcwd())
            print(msg)
            result = False

        return ""
    raise PreventUpdate



@callback(
    Output("log-output", "children"),
    Input("log-output-interval", "n_intervals"),
    State('btn_icon_ontology', 'n_clicks'),
)
def update_logs(n, btn):
    patched_children = Patch()
    
    if btn is None: 
        raise PreventUpdate
    
    log_buffer.seek(0)
    logs = log_buffer.read()
    
    
    
    patched_children.append(logs)
    
    return patched_children



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
                                    dmc.Button(
                                        id={"type": "btn_attachment", "index": n_clicks},
                                        children = dmc.Text(f"{btn_name_ttl}.ttl", td="underline"),
                                        leftSection= DashIconify(icon="hugeicons:attachment-square", width=20, color="grey"),
                                        variant="transparent",
                                        n_clicks=0
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
    Input("btn_icon_ontology", "n_clicks"),
    Input({"type": "btn_attachment", "index": ALL}, "n_clicks"),
    prevent_initial_call=True
)
def test(btn_prompt, n_clicks):
    
    if ctx.triggered_id == "btn_icon_ontology":
        raise PreventUpdate
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
                return dcc.send_file(os.getcwd()+f"/files/brick_{button_id['index']}.ttl")
            else:
                raise PreventUpdate
        

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