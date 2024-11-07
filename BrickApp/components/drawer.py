# import  dash_mantine_components as dmc



# data_llm_local = [["lama", "Lama"], ["a", "..."], ["b", "..."]]
# layout_ = dmc.Container(
#     children = [
#         # # dmc.Title("Model:", lh=1.2, order=2, mt="xs", fw=900, c="#e12024"),
#         # # dmc.Divider(variant = "solid", size="lg", mt=20, color="grey", pt=20, pl=20, pr=20, w="0%"),
#         # dmc.Title("Type of LLM",id="modalText1",lh=1.2, order=3, mt="xs", fw=900),
        
#         # dmc.SegmentedControl(
#         #     id="llm_model_type",
#         #     value="llm_model",
#         #     data=[
#         #         {"value": "llm_model", "label": "LLM"},
#         #         {"value": "local_model", "label": "Local LLM"}
#         #     ],
#         #     mb=10,
#         #     mt=20,
#         #     fullWidth=True,
#         #     style = {'width':'100%'},
#         #     radius="xl",
#         #     c='red'
#         # ),
#         # dmc.Select(
#         #     id="llm_model_",
#         #     label=dmc.Text(id="modalText2",children = "Select your favorite large language model"),
#         #     data=[
#         #         {'value':"openai","label":"OpenAI"},
#         #         {'value':"anthropic","label":"Anthropic"},
#         #         {'value':"fireworks","label":"Fireworks"},
#         #     ],
#         #     value="openai",
#         #     radius="lg",
#         #     placeholder="Pick values",
#         #     leftSectionPointerEvents="none",
#         #     leftSection=DashIconify(icon="fluent:brain-circuit-20-regular"),
#         #     comboboxProps={"shadow": "lg","transitionProps": { "transition": 'pop', "duration": 200 }},
#         #     style = {'color':'white'}
#         # ),
#         # dmc.Select(
#         #     id="llm_model_version",
#         #     label=dmc.Text(id="modalText3",children = "Select GPT model"),
#         #     radius="lg",
#         #     data = [
#         #         {'value':"gpt-4o", "label": "GPT 4o"},
#         #         {'value':"gpt-4", "label": "GPT 4"},
#         #     ],
#         #     value = "gpt-4o",
#         #     placeholder="Pick values",
#         #     leftSectionPointerEvents="none",
#         #     leftSection=DashIconify(icon="fluent:brain-circuit-20-regular"),
#         #     comboboxProps={"shadow": "lg","transitionProps": { "transition": 'pop', "duration": 200 }},
#         #     style = {'color':'white'}
#         # ),
#         # dmc.Select(
#         #     id="llm_model_local_huggin",
#         #     label=dmc.Text(id="modalText3",children = "Available local trained model:"),
#         #     data=[
#         #         {'value':"model1Huggin","label":"Ollama_1"},
#         #         {'value':"model2Huggin","label":"Ollama_2"},
#         #         {'value':"model3Huggin","label":"Ollama_3"},
#         #     ],
#         #     value="model1Huggin",
#         #     radius="lg",
#         #     placeholder="Local trained models",
#         #     leftSectionPointerEvents="none",
#         #     leftSection=DashIconify(icon="octicon:ai-model-24"),
#         #     comboboxProps={"shadow": "lg","transitionProps": { "transition": 'pop', "duration": 200 }},
#         #     mt=10
#         # ),
#         # dmc.TextInput(
#         #     id="api-key_value",
#         #     label = dmc.Text("API KEY:",id="text1", opacity=0.7, fw=700),
#         #     placeholder = "exeample: sk-example-1234567890abcdef1234567890abcdef",
#         #     leftSection=DashIconify(icon="carbon:api-key"),
#         #     mt=10,
#         #     radius="lg",
#         #     persistence=True,
#         #     persistence_type="session",
#         #     c="red"
#         # ),
            
#         # dmc.Divider(variant="solid",size="lg", mt=20, color="grey", pt=20, pl=20, pr=20, w="100%"),

#         # dmc.Button(
#         #     id="confirm_model", children = "CONFIRM", fullWidth=True, radius="lg", style = {'backgroundColor':'red', "color":"white"}
#         # )
#     ]
# )

# Drawer = dmc.Drawer(
#     id="drawer-simple",
#     padding="md",
#     size="30%",
#     title = dmc.Stack(
#         children = [
#             dmc.Title("Model", lh=1.2, order=2, mt="xs", fw=900, c="#e12024"),
#             dmc.Divider(variant = "solid", size="lg", mt=5, color="grey", pt=20, pl=20, pr=20, w="0%")
#             ]
#     ),
#     position="right",
#     children = [
#         layout_
#     ],
#     withCloseButton = True,
# )