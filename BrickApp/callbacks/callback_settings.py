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

@callback(
    Output("llm_model_", "style"),
    Output("upload_llm_local_model", "style"),
    Output("llm_local_model", "style"),
    Output("title_model_upload", "style"),
    Output("titles_token", "style"),
    Output("area_token", "style"),
    Input("llm_model_type","value"),
    prevent_intial_call=True
)
def input_model_selected(value_model):
    '''
    Different inputs according to model selection 
    '''
    if value_model == "llm_model":
        return display_on, display_off, display_off, display_off, display_on, display_on
    else:
        return display_off, style_drag_drop, display_on, display_off, display_off, display_off


@callback(
    Output("drawer-simple", "opened"),
    Input("setting", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True