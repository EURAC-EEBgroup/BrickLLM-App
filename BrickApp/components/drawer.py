from dash import html, dcc
import  dash_mantine_components as dmc



data_llm = [["openai", "OpenAI"], ["anthropic", "Anthropic"], ["fireworks", "Fireworks"]]
data_llm_local = [["lama", "Lama"], ["a", "..."], ["b", "..."]]
layout_ = dmc.Container(
    children = [
        dmc.Paper(
            children = [
                dmc.Title("Model:", lh=1.2, order=2, mt="xs", fw=900, c="#e12024"),
                dmc.Divider(variant = "solid", size="lg", mt=20, color="grey", pt=20, pl=20, pr=20, w="0%"),
                dmc.SegmentedControl(
                    id="llm_model_type",
                    value="llm_model",
                    data=[
                        {"value": "llm_model", "label": "LLM"},
                        {"value": "local_model", "label": "Local LLM"}
                    ],
                    mb=10,
                    mt=20,
                    fullWidth=True,
                    style = {'width':'100%'}
                ),
                # dmc.Paper(
                #     children = [
                        
                #     ],
                #     radius="lg",
                #     p=10,
                #     # m=5,
                #     w="100%",
                #     bg="#cccccc"
                # ),
                dmc.Title("Select type of LLM", lh=1.2, order=3, mt="xs", fw=900, c="black"),
                # dmc.Divider(variant = "solid", size="lg", mt=20, color="grey", pt=20, pl=20, pr=20),
                # html.Div(id="type_model_selection"),
                dmc.RadioGroup(
                    id="llm_model_",
                    children=dmc.Group([dmc.Radio(l, value=k) for k, l in data_llm], my=10),
                    value="openai",
                    label="Select your favorite large language model",
                    size="md",
                    w="100%"
                ),                
                dmc.RadioGroup(
                    id="llm_local_model",
                    children=dmc.Group([dmc.Radio(l, value=k) for k, l in data_llm_local], my=10),
                    value="lama",
                    label="Select your local large language model",
                    size="md",
                    w="100%"
                ),  
                dmc.Title(id="title_model_upload", children = "Upload your model", order=4, mb=20),
                dcc.Upload(
                    id='upload_llm_local_model',
                    children=dmc.Text(['Drag and Drop or ',html.A('Select Files')]),
                    style={"width":"100%"},
                    # Allow multiple files to be uploaded
                    multiple=True
                ),
                html.Div(
                    id="titles_token",
                    children = [
                        dmc.Title("TOKEN", lh=1.2, order=3, mt="xs", fw=900, c="black"),
                        dmc.Title("Provide your own token to use the LLM API", c="grey", opacity=0.7, fw=700, size="md",mt=5),
                    ]
                ),
                dmc.Textarea("sk-example-1234567890abcdef1234567890abcdef",id="area_token", w='100%', mt=20, placeholder=""),
                dmc.Divider(variant="solid",size="lg", mt=20, color="grey", pt=20, pl=20, pr=20, w="100%"),
                dmc.Button(
                    id="btn_confirm_model",
                    children = "CONFIRM",
                    fullWidth=True,
                    radius="lg",
                    style = {'backgroundColor':'#e12024'},
                    mt=10
                ),
            ],
            p="xl",
            mt= 10,
            mb= 10,
            radius="md",
            style={
                "backgroundColor":'white',
                "display": "flex",
                "flexDirection": "column",
                "justifyContent": "space-between",
                "alignItems": "flex-start",
                "backgroundSize": "cover",
                "backgroundPosition": "center",
            },
        )
    ]
)

Drawer = dmc.Drawer(
    id="drawer-simple",
    padding="md",
    size="40%",
    position="right",
    children = [
        layout_
    ],
    withCloseButton = True,
)