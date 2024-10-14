from dash import Output, Input, State, ctx, callback
import dash_mantine_components as dmc

display_on = {'display':'block'}
display_off = {'display':'none'}
style_drag_drop ={
    "border-style": "dashed",
    "width": "100% !important",
    "text-align": "center",
    "border-width": "1px",
    "border-radius": "5px",
    "margin": "10px",
    "padding": "10px",
    "height": "47px", 
    'display':'block'
}

# @callback(
#     Output("llm_model_", "style"),
#     Output("upload_llm_local_model", "style"),
#     Output("llm_local_model", "style"),
#     # Output("title_model_upload", "style"),
#     Output("titles_token", "style"),
#     Output("area_token", "style"),
#     Input("llm_model_type","value"),
#     prevent_intial_call=True
# )
# def input_model_selected(value_model):
#     '''
#     Different inputs according to model selection 
#     '''
#     if value_model == "llm_model":
#         return display_on, display_off, display_off, display_on, display_on
#     else:
#         return display_off, style_drag_drop, display_on, display_off, display_off


@callback(
    Output("drawer-simple", "opened"),
    Input("setting", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True


@callback(
    Output("llm_model_", "data"),
    Output("llm_model_", "value"),
    Output("llm_model_local_huggin","display"),
    Output("api-key_value","display"),
    Input("llm_model_type","value")
)
def types_of_llm_to_be_used(llm_selected):
    if llm_selected == "llm_model":
        data=[
                {'value':"openai","label":"OpenAI"},
                {'value':"anthropic","label":"Anthropic"},
                {'value':"fireworks","label":"Fireworks"},
            ]
        value="openai"
        hug_models = "none"
        api_key = True
    else: 
        data = [
            {'value':'ollama', 'label':'Ollama 3.1'}
        ]
        value="ollama"
        hug_models = True,
        api_key = "none"
    return data, value, hug_models, api_key

@callback(
    Output("llm_model_version","display"),
    Input("llm_model_","value"),
)
def display_options(llModel):
    if llModel == "openai":
        return True
    return "none"

# @callback(
#     Output("llm_model_version","data"),
#     Output("llm_model_version","value"),
#     Input("llm_model_","value"),
#     prevent_initial_call=True
# )
# def type_of_GPT(llModel):
#     ''' Different GPT accroding to the type of choice'''
#     if llModel == "openai":
#         data = [
#             {'value':"gpt-4o", "label": "GPT 4o"},
#             {'value':"gpt-4", "label": "GPT 4"},
#         ]
#         value = "gpt-4o"
#     else: 
#         data=[
#             {'value':"test", "label": "Test"},
#         ],
#         value="test"
    
#     return data, value