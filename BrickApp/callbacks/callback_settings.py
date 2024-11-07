from dash import Output, Input, State, ctx, callback, get_relative_path
from dash.exceptions import PreventUpdate 
from urllib.parse import urlparse

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

@callback(
    Output("llm_model_", "data"),
    Output("llm_model_", "value"),
    Output("llm_model_local_huggin","display"),
    Output("llm_model_version","display"),
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
        model_version=True
    else: 
        data = [
            {'value':'ollama', 'label':'Ollama 3.1'}
        ]
        value="ollama"
        hug_models = True,
        api_key = "none"
        model_version="none"
    return data, value, hug_models, model_version, api_key



@callback(
    Output("menu_mobile","style"),
    Output("burger_mobile","style"),
    Input("url_app", "href")
)
def remove_menu_no_home_page(href):
    display_no = {'display':'none'}
    dispaly_block = {'display': 'block'}
    parsed_url = urlparse(href)
    # Extract the path
    path = parsed_url.path
    if path == get_relative_path("/contact") or path == get_relative_path("/terms&condition") or path == get_relative_path("/aknowledgments"):
        return display_no,display_no
    else:
        return dispaly_block, dispaly_block