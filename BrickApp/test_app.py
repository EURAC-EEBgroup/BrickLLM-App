# import dash
# from dash import html, dcc, Output, Input, callback
# import dash_mantine_components as dmc
# from dash_iconify import DashIconify

# # Including Font Awesome
# dash._dash_renderer._set_react_version("18.2.0")
# app = dash.Dash(__name__)

# app.layout =  dmc.MantineProvider(
#     dmc.Container(
#         size="md",
#         children = [
            
#             html.Button("Click Me", id="fade-button", n_clicks=0),
#             dmc.ActionIcon(
#                 id="icon-to-fade",
#                 children = DashIconify(id="icon_run", icon="fa6-solid:trowel-bricks",width=25, rotate=0, color="black", flip="horizontal"),
#                 size="xl",
#                 variant="transparent",
#             ),
#         ]
#     )
    
# )

# @app.callback(
#     Output("icon-to-fade", "style"),
#     Input("fade-button", "n_clicks"),
#     prevent_initial_call=True
# )
# def fade_icon(n_clicks):
#     if n_clicks > 0:
#         return {'font-size': '24px', 'transition': 'opacity 2s', 'opacity': 0}
#     return {'font-size': '24px', 'transition': 'opacity 2s', 'opacity': 1}

# if __name__ == '__main__':
#     app.run_server(debug=True, port=8051)

# import dash
# from dash import html, dcc, Input, Output, callback
# import dash_bootstrap_components as dbc

# # Initialize the Dash app with Bootstrap for styling
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# app.layout = html.Div([
#     dcc.Textarea(
#         id='input-textarea',
#         value='',
#         style={'width': '100%', 'height': 100},
#         placeholder="Type something here..."
#     ),
#     html.Div(
#         children=[html.I(className="fas fa-check-circle")],
#         id='icon-container',
#         style={'color': 'green', 'fontSize': 30}
#     )
# ])

# @app.callback(
#     Output('icon-container', 'style'),
#     Input('input-textarea', 'value')
# )
# def toggle_icon_visibility(value):
#     if value:
#         return {'color': 'green', 'fontSize': 30, 'transition': 'opacity 2s', 'opacity': 1}
#     else:
#         return {'color': 'green', 'fontSize': 30, 'transition': 'opacity 2s', 'opacity': 0}

# if __name__ == '__main__':
#     app.run_server(debug=True, port=8051)
from dash import Dash, html, dcc, Input, Output, State
import dash

# Initialize the app
app = Dash(__name__)

app.layout = html.Div([
    # Main Div Container (with scroll)
    html.Div(id='main-div', style={
        'height': '300px',  # Set a fixed height for the scrollable container
        'overflow-y': 'auto',  # Enable vertical scrolling
        'border': '1px solid black',
        'padding': '10px'
    }),
    
    # Button to add a new div
    html.Button('Add Element', id='add-button'),
    
    # Invisible div to trigger the scroll
    html.Div(id='dummy-div', style={'display': 'none'})
], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'})

# Callback to add a new div inside the main div
@app.callback(
    [Output('main-div', 'children'), Output('dummy-div', 'children', allow_duplicate=True)],
    [Input('add-button', 'n_clicks')],
    [State('main-div', 'children')],
    prevent_initial_call=True
)
def add_new_div(n_clicks, children):
    # Initialize children if it's None
    if children is None:
        children = []
    
    # Add a new div element to the main container
    new_div = html.Div(f'New Element {n_clicks}', style={'margin': '5px', 'background-color': 'lightgrey', 'padding': '10px'})
    children.append(new_div)
    
    # Return updated children and trigger for dummy div
    return children, ''


# JavaScript scroll function
app.clientside_callback(
    """
    function(n_clicks) {
        var mainDiv = document.getElementById('main-div');
        if (mainDiv) {
            mainDiv.scrollTop = mainDiv.scrollHeight;
        }
        return '';
    }
    """,
    Output('dummy-div', 'children'),
    Input('add-button', 'n_clicks')
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)



