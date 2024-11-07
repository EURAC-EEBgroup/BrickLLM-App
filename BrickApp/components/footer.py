import dash_mantine_components as dmc
from dash import html, get_relative_path


Footer =  dmc.AppShellFooter(
    id="footer__",
    h=180,
    zIndex=1001, 
    withBorder=True,
    children=[
        dmc.Container(
            size="xl",
            children = [
                dmc.Grid(
                    children = [
                        dmc.GridCol(
                            children = [
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
                                    size="xs",
                                    opacity=1,
                                    ml=5,
                                    c= "#069DC9"
                                )
                            ],
                            span=4,
                            mt=10,
                            ml=10,
                            # sm=
                        ),
                        dmc.GridCol(
                            children = [
                                dmc.Stack(
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
                            
                            ],
                            span=5
                        ),
                        dmc.GridCol(
                            children = [
                                dmc.Flex(
                                    children = [
                                        dmc.Divider(variant="solid", w=30, color="black",size="lg",mt=10),
                                        html.A(
                                            href = get_relative_path("/contact"),
                                            title="Contact",
                                            children=[
                                                html.Span("Contact")
                                            ],
                                            target="_blank"
                                        )
                                    ],
                                    justify={"sm": "flex-start"},
                                    gap="md"
                                ),
                                dmc.Flex(
                                    children = [
                                        dmc.Divider(variant="solid", w=30, color="black",size="lg",mt=10),
                                        html.A(
                                            href = get_relative_path("/terms&condition"),
                                            title="Terms",
                                            children=[
                                                html.Span("Terms and Condition")
                                            ],
                                            target="_blank"
                                        )
                                    ],
                                    justify={"sm": "flex-start"},
                                    gap="md"
                                ) 
                            ],
                            span=2
                        ),
                    ],
                    align="center"
                ),        
            ]
        ),
    ],
    style={
        "paddding": ["24px", "16px"],
        "backgroundColor": "white"
    }
)


footer_2 = html.Div(
    id="footer_grey",
    className="footer_bottom",
    style = {
        'backgroundColor':'#f0f1f1',
        'zIndex': 5
    },
    children = [
        html.Footer(
            children = [
                html.Div(
                    id="footer_up",
                    className = "footer_middle",
                    children = [
                        html.Div(
                            # className="container_center",
                            children = [
                                html.Div(
                                    className="footer_col_1",
                                    style = {'marginLeft':'20px'},
                                    children = [
                                        html.Div(className="textblock__5", children = "A platform by", style = {'color':'#333', 'marginLeft':'35px', 'marginTop':'10px'}),
                                        html.Div(className="textblock__5", children = "Developed thanks to", style = {'color':'#333', 'marginLeft':'35px', 'marginTop':'10px'}),
                                    ]
                                ),
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

footer_1 = html.Div(
    className="section_footer",
    children = [
        html.Footer(
            children = [
                html.Div(
                    className = "footer_middle",
                    children = [
                        html.Div(
                            className="container_center",
                            style = {'marginTop':'20px', 'marginLeft':'30px'},
                            children = [
                                html.Div(
                                    className="footer_col_1",
                                    children = [
                                        html.P(
                                            id="service_footer",
                                            className="footer_title",
                                            children = "Service"
                                        ),
                                        dmc.Group(
                                            id="service_footer_link",
                                            children = [
                                                html.Ul(
                                                    className="navispecial_footer_wrapper",
                                                    children = [
                                                        html.Li(
                                                            className="navispecial_item",
                                                            children = [
                                                                dmc.Anchor(
                                                                    "Contact",
                                                                    href=get_relative_path("/contact"),
                                                                ),
                                                                html.A(
                                                                    className="navispecial_link linkstyle linkstyle__1",
                                                                    href = get_relative_path("/contact"),
                                                                    title="Contact",
                                                                    children=[
                                                                        html.Span(
                                                                            "Contact",
                                                                        )
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                ),
                                html.Div(
                                    className="footer_col_1",
                                    children = [
                                        html.P(
                                            className = "footer_title",
                                            children = [
                                                html.Strong("Eurac Research"),
                                                html.Br(),
                                                " Viale Druso, 1/Drususallee 1",
                                                html.Br(), 
                                                " 39100 Bolzano/ Bozen - Italy",
                                                html.Br(), 
                                                " Tel: +39 0471 055 055",
                                                html.Br(),  
                                                " Fax: +39 0471 055 099",
                                                html.Br(), 
                                                " Email: ",
                                                html.A(
                                                    href = "mailto:daniele.antonucci@eurac.edu",
                                                    children = "daniele.antonucci@eurac.edu"
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)