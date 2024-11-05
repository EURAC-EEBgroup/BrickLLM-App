import dash_mantine_components as dmc
from dash import get_relative_path,dcc, html
from dash_iconify import DashIconify



header_flex = dmc.Flex(
    children = [
        dmc.ActionIcon(
            id= "burger_mobile",
            children = DashIconify(id="icon_burger",icon="circum:menu-burger", width=20, color="black"),
            variant="transparent",
            size="xl",
            mb=10,
            style = {
                'position':'absolute',
                'left':'0px'
            }
        ),
        dmc.Grid(
            children = [
                dmc.GridCol(
                    id="col_text_header",
                    children = [
                        dmc.Center(
                            id="title",
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
                        )       
                            
                    ],
                    style = {
                        "position": "absolute",
                        "display": "flex",
                    },
                    # span=10,
                    span={'base':10,'md':10,'sm':10},
                ),
                dmc.GridCol(
                    children = [
                        dmc.Menu(
                            [
                                dmc.MenuTarget(
                                dmc.ActionIcon(
                                    id="github",
                                    children = DashIconify(id="icon_git", icon="akar-icons:github-fill", width=40),
                                    variant="transparent",
                                    size="xl",
                                    # style = {'color':'#e12024'}, 
                                    style = {'color':'black', 'justifyContent':'end !important'}, 
                                ),
                                ),
                                dmc.MenuDropdown(
                                    children = [
                                        dmc.MenuItem(
                                            "BrickLLM - App ",
                                            href = "https://github.com/EURAC-EEBgroup/Brick_ontology_tool",
                                            target="_blank",
                                            leftSection=DashIconify(icon="carbon:application-web"),
                                        ),
                                        dmc.MenuItem(
                                            "BrickLLM - Library ",
                                            href = "https://github.com/EURAC-EEBgroup/brick-llm/tree/main",
                                            target="_blank",
                                            leftSection=DashIconify(icon="mdi:source-repository"),
                                        )

                                    ]
                                )
                            ]
                        ),
                        # dmc.Anchor(
                        #     dmc.ActionIcon(
                        #         id="github",
                        #         children = DashIconify(id="icon_git", icon="akar-icons:github-fill", width=40),
                        #         variant="transparent",
                        #         size="xl",
                        #         # style = {'color':'#e12024'}, 
                        #         style = {'color':'black', 'justifyContent':'end !important'}, 
                        #     ),
                        #     href = "https://github.com/EURAC-EEBgroup/brick-llm/tree/main",
                        #     target="_blank"
                        # ),
                        dmc.Menu(
                            id="menu_mobile",
                            children = [
                                dmc.MenuTarget(
                                    dmc.ActionIcon(
                                        id="menu_mobile_button",
                                        children = DashIconify(id="icon_menu_mobile", icon="ph:dots-three-vertical-bold", width=40),
                                        variant="transparent",
                                        size="xl", 
                                        style = {'color':'black'},
                                    ),  
                                ),
                                dmc.MenuDropdown(
                                    [
                                        dmc.Anchor(
                                            dmc.MenuItem("Terms and Condition", leftSection=DashIconify(icon="hugeicons:legal-02")),
                                             href="/terms_condition",
                                            target="_blank"
                                        ),
                                        dmc.Anchor(
                                            dmc.MenuItem("Contact", leftSection=DashIconify(icon="weui:contacts-outlined")),
                                            href = "/contact",
                                            target="_blank"
                                        )
                                    ]
                                )
                            ]
                        )
                        
                    ],
                    style = {
                        'position':'absolute',
                        'right':'0px',
                        'display':'flex',
                        'justifyContent':'flex-end'
                    },
                    span={'base':1,'md':2,'sm':2},
                )
            ]
        )
    ]
)

Header = dmc.AppShellHeader(
    id="header_app",
    h=80,
    p=20,
    children = header_flex
)

# Header = dmc.AppShellHeader(
#     id="header_app",
#     h=80,
#     p=20,
#     children = [
#         dmc.Group(
#             children = [
#                 dmc.ActionIcon(
#                     id= "burger_mobile",
#                     children = DashIconify(icon="stash:burger-classic-duotone", width=20, color="black"),
#                     variant="transparent",
#                     size="xl",
#                     mb=10,
#                 ),
#                 html.Div(
#                     className="row",
#                     children = [
#                         html.Div(
#                         className="col-lg-11 col-md-8 col-sm-8",
#                         children =[
#                             dmc.Group(
#                                 children = [
#                                     dmc.Center(
#                                         id="title",
#                                         children = [
#                                             dmc.Flex(
#                                                 direction="column",
#                                                 w="100%",
#                                                 children = [
                                                    
#                                                     dmc.Text("PROMPTING",id="text1", opacity=0.7, fw=700, c="black"),
#                                                     dmc.Title("Write text to generate brick ontology", id="text2",lh=1.2, order=3, mt=0, fw=900, c="black"),
#                                                     # dmc.Divider(variant = "solid", size="lg", mt=20, color="grey", pt=20, pl=20, pr=20),
#                                                 ]
#                                             ),
#                                         ]
#                                     )       
#                                 ],
#                                 gap="xs",
#                                 style = {
#                                     "position": "absolute",
#                                     "left": "0px",
#                                     "display": "flex",
#                                 }
#                             )
#                         ]
#                         ),
#                         html.Div(
#                             className="col-lg-1 col-md-2, col-sm-2",
#                             children = [
#                                 dmc.Anchor(
#                                     dmc.ActionIcon(
#                                         id="github",
#                                         children = DashIconify(id="icon_git", icon="akar-icons:github-fill", width=40),
#                                         variant="transparent",
#                                         size="xl",
#                                         # style = {'color':'#e12024'}, 
#                                         style = {'color':'black'}, 
#                                     ),
#                                     href = "https://github.com/EURAC-EEBgroup/brick-llm/tree/main",
#                                     target="_blank"
#                                 ),
                                
                                
#                             ],
#                             style = {
#                                 'position':'absolute',
#                                 'right':'0px',
#                                 'display':'flex',
#                                 'justifyContent':'flex-end'
#                             }
#                         )
#                     ]
#                 )
#             ]
#         )
#     ]
# )

    #     dmc.Grid(
    #         children = [
    #             dmc.GridCol(
    #                 children = [
    #                     dmc.Center(
    #                         children = [
    #                             dmc.Flex(
    #                                 direction="column",
    #                                 w="100%",
    #                                 children = [
    #                                     dmc.Text("PROMPTING",id="text1", opacity=0.7, fw=700, c="black"),
    #                                     dmc.Title("Write text to generate brick ontology", id="text2",lh=1.2, order=3, mt=0, fw=900, c="black"),
    #                                     # dmc.Divider(variant = "solid", size="lg", mt=20, color="grey", pt=20, pl=20, pr=20),
    #                                 ]
    #                             ),
    #                         ]
    #                      ),
    #                 ],
    #                 # children = [
    #                 #     dmc.Anchor(
    #                 #         href = "/",
    #                 #         children = [
    #                 #             dmc.Image(
    #                 #                 src = "/assets/Brick_1.png",
    #                 #                 h=80,
    #                 #                 w="auto",mt=0
    #                 #             )                                                                                                                                       
    #                 #         ]
    #                 #     )
    #                 # ],
    #                 span=7
    #             ),
    #             dmc.GridCol(span="content"),
    #             dmc.GridCol(
    #                 children = [
    #                     dmc.Anchor(
    #                         dmc.ActionIcon(
    #                             id="github",
    #                             children = DashIconify(icon="akar-icons:github-fill", width=40),
    #                             variant="transparent",
    #                             size="xl",
    #                             # style = {'color':'#e12024'}, 
    #                             style = {'color':'black'}, 
    #                         ),
    #                         href = "https://github.com/EURAC-EEBgroup/brick-llm/tree/main",
    #                         target="_blank"
    #                     ),
    #                     dmc.ActionIcon(
    #                         id="burger_mobile",
    #                         children = DashIconify(icon="stash:burger-classic-duotone", width=30),
    #                         variant="transparent",
    #                         size="xl"
    #                     ),
    #                 ],
    #                 span=1,
    #                 style = {
    #                     'position':'absolute',
    #                     'right':'10px'
    #                 }
    #             )
    #         ]
    #     )
    # ]

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
# )