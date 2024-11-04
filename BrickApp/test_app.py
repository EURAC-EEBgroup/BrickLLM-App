import base64
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H3("Select Files from a Folder"),
    dcc.Upload(
        id="upload-folder",
        children=html.Button("Choose Folder"),
        multiple=True,  # Allow multiple files to be uploaded
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        }
    ),
    html.Div(id="output-folder")
])

@app.callback(
    Output("output-folder", "children"),
    [Input("upload-folder", "contents")],
    [State("upload-folder", "filename")]
)
def show_folder(contents, filenames):
    if contents is not None:
        # Extract folder names from filenames
        folder_names = set()
        for filename in filenames:
            # Extract the folder part from the filename
            folder = filename.split('/')[0] if '/' in filename else filename.split('\\')[0]
            folder_names.add(folder)

        return html.Div([html.P(f"Detected Folder: {folder}") for folder in folder_names])
    return "No folder selected"

if __name__ == '__main__':
    app.run_server(debug=True)
