from dash import Output, Input, State, ctx, callback, dcc,  ALL, Patch, MATCH, no_update, set_props
from dash.exceptions import PreventUpdate
import io
from brickllm.graphs import BrickSchemaGraph
import sys
import os
import dash_mantine_components as dmc


def get_card(index):
    card =  dmc.Card(
        id={"type": "card", "index": index},
        className="single_test_card",
        children=[
            dmc.Text(f"card n. {index}"),
            dmc.Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
        ]
    )
    return card


@callback(
    Output("first-child", "children"),
    Input("btn_add_card", "n_clicks"),
)
def add_card(btn):
    if btn is None: 
        raise PreventUpdate
    
    index = btn
    patched_children = Patch()
    card = get_card(index)
    patched_children.insert(0, card)

    return patched_children