import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Textarea(
        id='dynamic-textarea',
        value='Type here...',
        style={
            'width': '100%',
            'min-height': '50px',  # Set a minimum height
            'overflow': 'hidden',  # Prevent scrolling
        }
    ),
    html.Div(id='output-container')
])

@app.callback(
    Output('output-container', 'children'),
    Input('dynamic-textarea', 'value')
)
def update_output(value):
    return f'You have entered: {value}'

# JavaScript for auto-resizing textarea
app.clientside_callback(
    """
    function(value) {
        var textarea = document.getElementById('dynamic-textarea');
        textarea.style.height = 'auto';  // Reset height to auto to recalculate
        textarea.style.height = textarea.scrollHeight + 'px';  // Set height to scrollHeight
        return value;  // Return the value to keep the callback functional
    }
    """,
    Output('dynamic-textarea', 'value'),
    Input('dynamic-textarea', 'value')
)

if __name__ == '__main__':
    app.run_server(debug=True)
