import dash_mantine_components as dmc
from dash import get_relative_path,dcc
from dash_iconify import DashIconify

Header = dmc.AppShellHeader(
    id="header_app",
    h=80,
    p=20,
    children = [
        dmc.Grid(
            children = [
                dmc.GridCol(
                    children = [
                        dmc.Center(
                            children = [
                                dmc.Flex(
                                    direction="column",
                                    w="100%",
                                    children = [
                                        dmc.Text("PROMPTING",id="text1", opacity=0.7, fw=700, c="black"),
                                        dmc.Title("Write text to generate brick ontology", id="text2",lh=1.2, order=3, mt=0, fw=900, c="black"),
                                        # dmc.Divider(variant = "solid", size="lg", mt=20, color="grey", pt=20, pl=20, pr=20),
                                    ]
                                ),
                            ]
                         ),
                    ],
                    # children = [
                    #     dmc.Anchor(
                    #         href = "/",
                    #         children = [
                    #             dmc.Image(
                    #                 src = "/assets/Brick_1.png",
                    #                 h=80,
                    #                 w="auto",mt=0
                    #             )
                    #         ]
                    #     )
                    # ],
                    span=7
                ),
                dmc.GridCol(span=2),
                dmc.GridCol(
                    children = [
                        dmc.Anchor(
                            dmc.ActionIcon(
                                id="github",
                                children = DashIconify(icon="akar-icons:github-fill", width=40),
                                variant="transparent",
                                size="xl",
                                # style = {'color':'#e12024'}, 
                                style = {'color':'black'}, 
                            ),
                            href = "https://github.com/EURAC-EEBgroup/brick-llm/tree/main",
                            target="_blank"
                        ),
                    ],
                    span=1,
                    style = {
                        'position':'absolute',
                        'right':'10px'
                    }
                )
            ]
        )
    ]

        # dmc.Group(
        #     children = [
        #         dcc.Link(
        #             id="link_eurac5",
        #             children = [
        #                 dmc.Anchor(
        #                     href = "www.eurac.edu",
        #                     children = [
        #                         dmc.Image(
        #                             id="logo_header",
        #                             h=50,
        #                         )
        #                     ]
        #                 )
        #             ],
        #             href = "www.eurac.edu",
        #         ),
        #         dmc.Group(
        #             children = [
        #                 dmc.Anchor(
        #                     dmc.ActionIcon(
        #                         id="github",
        #                         children = DashIconify(icon="akar-icons:github-fill", width=25),
        #                         variant="transparent",
        #                         style = {'color':'#e12024'}, 
        #                     ),
        #                     href = "https://github.com/EURAC-EEBgroup/brick-llm/tree/main",
        #                     target="_blank"
        #                 ),
        #                 dmc.ActionIcon(
        #                     id="setting",
        #                     children = DashIconify(icon="lets-icons:setting-fill", width=30),
        #                     variant="transparent",
        #                     style = {'color':'#e12024','marginBottom':'5px'}, 
        #                 )
        #             ]
        #         )
        #         # DashIconify(icon="", width=100),
        #         # dmc.ActionIcon(
        #         #     [
        #         #         dmc.Paper(DashIconify(icon="radix-icons:sun", width=25), darkHidden=True),
        #         #         dmc.Paper(DashIconify(icon="radix-icons:moon", width=25), lightHidden=True),
        #         #     ],
        #         #     variant="transparent",
        #         #     color="yellow",
        #         #     id="color-scheme-toggle",
        #         #     size="lg",
        #         #     ms="auto",
        #         #     style = {'display':'none'}
        #         # ),
                
        #     ],
        #     justify="space-around"
        # )
)