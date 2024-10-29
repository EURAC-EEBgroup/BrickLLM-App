import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import time
import threading

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-command', type='text', value='echo Hello, World!'),
    html.Button('Run Command', id='run-button', n_clicks=0),
    dcc.Textarea(id='output-area', style={'width': '100%', 'height': '300px'}, value='', readOnly=True)
])

def simulate_terminal_output(command, update_output):
    # Simulate processing the command
    output = f"Running command: {command}\n"
    time.sleep(1)  # Simulate time delay for processing
    # Simulate command output
    if command.startswith('echo'):
        output += command[5:] + '\n'
    else:
        output += f"Command not found: {command}\n"
    update_output(output)

@app.callback(
    Output('output-area', 'value'),
    Input('run-button', 'n_clicks'),
    Input('input-command', 'value')
)
def run_command(n_clicks, command):
    if n_clicks > 0:
        output = []
        
        # Create a function to update output from the thread
        def update_output(new_output):
            nonlocal output
            output.append(new_output)

        # Start a thread to simulate terminal output
        threading.Thread(target=simulate_terminal_output, args=(command, lambda x: update_output(x))).start()
        
        return '\n'.join(output)  # Return current output
    return ''  # Return empty if no button click

if __name__ == '__main__':
    app.run_server(debug=True)
