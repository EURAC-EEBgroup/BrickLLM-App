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