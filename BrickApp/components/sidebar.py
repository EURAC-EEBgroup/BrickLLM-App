import dash_mantine_components as dmc
from dash import html, dcc
from dash_iconify import DashIconify
import dash_daq as daq

layout_ = dmc.Container(
    children = [
        dmc.Title("Type of LLM",id="modalText1",lh=1.2, order=3, mt="xs", fw=900),
        
        dmc.SegmentedControl(
            id="llm_model_type",
            value="llm_model",
            data=[
                {"value": "llm_model", "label": "LLM"},
                {"value": "local_model", "label": "Local LLM"}
            ],
            persistence= True,
            persistence_type = "session",
            mb=10,
            mt=20,
            fullWidth=True,
            style = {'width':'100%'},
            radius="xl",
            c='red'
        ),
        dmc.Select(
            id="llm_model_",
            label=dmc.Text(id="sidebarText2",children = "Select your favorite large language model"),
            data=[
                {'value':"openai","label":"OpenAI"},
                {'value':"anthropic","label":"Anthropic"},
                {'value':"fireworks","label":"Fireworks"},
            ],
            value="openai",
            radius="lg",
            placeholder="Pick values",
            leftSectionPointerEvents="none",
            leftSection=DashIconify(icon="fluent:brain-circuit-20-regular"),
            comboboxProps={"shadow": "lg","transitionProps": { "transition": 'pop', "duration": 200 }},
            style = {'color':'white'}
        ),
        dmc.Select(
            id="llm_model_version",
            label=dmc.Text(id="sidebarText3",children = "Select GPT model"),
            radius="lg",
            data = [
                {'value':"gpt-4o", "label": "GPT 4o"},
                {'value':"gpt-4", "label": "GPT 4"},
            ],
            value = "gpt-4o",
            placeholder="Pick values",
            leftSectionPointerEvents="none",
            leftSection=DashIconify(icon="fluent:brain-circuit-20-regular"),
            comboboxProps={"shadow": "lg","transitionProps": { "transition": 'pop', "duration": 200 }},
            style = {'color':'white'}
        ),
        dmc.Select(
            id="llm_model_local_huggin",
            label=dmc.Text(id="sidebarText4",children = "Available local trained model:"),
            data=[
                {'value':"llama3.1:8b-brick-v8","label":"llama3.1:8b-brick-v8"},
            ],
            value="llama3.1:8b-brick-v8",
            radius="lg",
            placeholder="Local trained models",
            leftSectionPointerEvents="none",
            leftSection=DashIconify(icon="octicon:ai-model-24"),
            comboboxProps={"shadow": "lg","transitionProps": { "transition": 'pop', "duration": 200 }},
            mt=10
        ),
        dmc.PasswordInput(
            id="api-key_value",
            label=dmc.Text("API KEY:",id="sidebarText5", fw=700),
            placeholder="exeample: sk-example-1234567890abcdef1234567890abcdef",
            leftSection=DashIconify(icon="carbon:api-key"),
            mt=10,
            persistence=True,
            persistence_type="session",
            radius="lg",
        ),
            
        dmc.Divider(variant="solid",size="lg", mt=20, color="grey", pt=20, pl=20, pr=20, w="100%"),
        # daq.ToggleSwitch(
        #     id='btn_confirm_model',
        #     value=False,
        #     label="Confirm selection",
        #     labelPosition ="bottom",
        #     color="rgb(6, 157, 201)",
        #     theme="dark",
        #     persistence=True,
        #     persistence_type="session" 
        # ),
        dmc.Switch(
            id = "btn_confirm_model",
            size="md",
            radius="xl",
            label=dmc.Text(id="confirmSelection", children = "Confirm selection"),
            checked=False,  
            color="rgb(6, 157, 201)",
            persistence=True,
            persistence_type="session"        
        ),
        html.Div(id="local_warning_time")
    ]
)

# Sidebar = dmc.AppShellAside(
#     id="sidebar_",
#     children = [
#         dmc.Stack(
#             id="test",
#             children = [
#                 layout_
#             ]
#         )
#     ]
# )

