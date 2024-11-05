from dash import Output, Input, State, ctx, callback
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
    Output("burger_mobile","style"),
    Output("menu_mobile_button","style"),
    Input("url_app","href")
)
def delete_burger_drawer_contact(url):
    style_ = {'display':'none'}
    style_b = {'display':'block'}
    if urlparse(url).path=="/contact":
        return style_, style_
    raise PreventUpdate
