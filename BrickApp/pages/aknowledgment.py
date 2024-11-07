from dash import html, get_relative_path
import dash_mantine_components as dmc
import dash 
from dash_iconify import DashIconify
dash.register_page(__name__,path_template=f"/aknowledgments")

developed_by = dmc.Stack(
    children = [
        dmc.Text("Developed by:", size="md", fw=600, c="black", opacity=0.9),
        dmc.Flex(
            children = [
                dmc.Anchor(
                    children = [
                        dmc.Image(
                            src = get_relative_path("/assets/eurac_logo_grey_WEB_pos.png"),
                            h=50,
                            w="auto"
                        ),
                    ],
                    href="https://www.eurac.edu/en/institutes-centers/institute-for-renewable-energy/research-group/energy-efficient-buildings",
                    target="_blank"
                ),
                
                dmc.Anchor(
                    children = [
                        dmc.Image(
                            src = get_relative_path("/assets/logo_polito.png"),
                            h=70,
                            w="auto"
                        )
                    ],
                    href = "http://www.baeda.polito.it/research",
                    target="_blank"
                )
            ],
            justify={"sm": "center"},
            direction={"base": "column", "sm": "row"},
            gap="xl"
        )
    ]
)

thanks_to = dmc.Stack(
    children = [
        dmc.Text("Thanks to:", size="md", fw=600, c="black", opacity=0.9),
        dmc.Center(
            children = [
                dmc.Anchor(
                    href = "https://moderate-project.eu/",
                    children = [
                        dmc.Image(
                            src = get_relative_path("/assets/moderate_logo.png"),
                            h=50,
                            w="auto"
                        )
                    ],
                    mb=5
                ),
            ]
        ),
        dmc.Text(
            id="text_moderate",
            children="Horizon Europe research and innovation programme under grant agreement No 101069834. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or CINEA. Neither the European Union nor the granting authority can be held responsible for.",
            opacity=1,
            ml=5,
            c= "#069DC9",
            style = {'fontSize':'1rem'}
        )
    ],
    mt=20
)



layout_ = dmc.Container(
    mt=90, 
    children = [
        dmc.Text("AKNOWLEDGMENTS",id="text1", opacity=0.7, fw=700, c="black"),
        dmc.Title("BRICK - LLM", id="text2",lh=1.2, order=3, mt="xs", fw=900, c="black"),
        dmc.Divider(variant = "solid", size="lg", mt=20, color="grey", pt=20, pl=20, pr=20),
        developed_by,
        thanks_to
    ]
)

def layout():
    return layout_