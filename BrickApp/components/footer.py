import dash_mantine_components as dmc
from dash import html, get_relative_path, dcc

Footer =  dmc.AppShellFooter(
    h=180,
    zIndex=1000, 
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
                                            href = "www.eurac.edu",
                                            children = [
                                                dmc.Image(
                                                    src = "/assets/moderate_logo.png",
                                                    h=50,
                                                    w="auto"
                                                )
                                            ],
                                            mb=5
                                        ),
                                    ]
                                ),
                                dmc.Text(
                                    children="Horizon Europe research and innovation programme under grant agreement No 101069834. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or CINEA. Neither the European Union nor the granting authority can be held responsible for.",
                                    size="xs",
                                    opacity=1,
                                    ml=5,
                                    c= "#069DC9"
                                )
                            ],
                            span=4,
                            mt=10,
                            ml=10
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
                                                            src = "/assets/eurac_logo_grey_WEB_pos.png",
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
                                                            src = "/assets/logo_polito.png",
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
                                            href = "/contact",
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
                                            href = "/terms&condition",
                                            title="Terms",
                                            children=[
                                                html.Span("Terms")
                                            ],
                                            target="_blank"
                                        )
                                        # dmc.Text("Terms",size="lg", c="black", w=700, opacity=0.9),
                                        # dcc.Link(
                                        #     children = 
                                        #     href="/contact"
                                        # )
                                    ],
                                    justify={"sm": "flex-start"},
                                    gap="md"
                                ) 
                            ],
                            span=2
                        ),
                    ],
                    # justify="center",
                    align="center"
                ),        
            ]
        ),
        # dmc.Divider(variant="solid", c="black", size="md", mt=5, mb=5),
        # dmc.Text(
        #     html.A(
        #         "Copyright © Eurac Research",
        #         href="http://www.eurac.edu/en/pages/default.aspx",
        #         style={
        #             "color": "grey",
        #         }
        #     ),
        #     mb=5,
        #     style={
        #         "textAlign": "center"
        #     }
        # ),
        # dmc.Container(
        #     children=[
        #         html.Div(
        #             [
        #                 dmc.Text(
        #                     html.A(
        #                         "Copyright © Eurac Research",
        #                         href="http://www.eurac.edu/en/pages/default.aspx",
        #                         style={
        #                             "color": "#CC3425",
        #                         }
        #                     ),
        #                     style={
        #                         "textAlign": "center"
        #                     }
        #                 ),
        #             ]
        #         )
        #     ],
        #     style={
        #         "maxWidth":"600px",
        #         "paddingLeft": "24px",
        #         "paddingRight": "24px",
        #         "display": "flex",
        #         "flexDirection": "column"
        #     }
        # )
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
                                        # dmc.Image(
                                        #     src=get_relative_path("/assets/eurac_logo.png"),
                                        #     mt=0,
                                        #     w=200,
                                        # ),
                                        html.Div(className="textblock__5", children = "Developed thanks to", style = {'color':'#333', 'marginLeft':'35px', 'marginTop':'10px'}),
                                        # dmc.Group(
                                        #     children = [
                                        #         dmc.Image(
                                        #             src=get_relative_path("/assets/EU_COF.png"),
                                        #             mt=0,
                                        #             w=300,
                                        #         ),
                                        #         dmc.Image(
                                        #             src=get_relative_path("/assets/iwg5_1.png"),
                                        #             mt=0,
                                        #             w=300,
                                        #         ),
                                        #     ],
                                        #     style = {'marginLeft':'25px'}
                                        # )
                                    ]
                                ),
                                # html.Div(
                                #     className="footer_col_1",
                                #     children = [
                                #         html.P(
                                #             className = "footer_title",
                                #             children = [
                                #                 html.Strong("Eurac Research"),
                                #                 html.Br(),
                                #                 " Viale Druso, 1/Drususallee 1",
                                #                 html.Br(), 
                                #                 " 39100 Bolzano/ Bozen - Italy",
                                #                 html.Br(), 
                                #                 " Tel: +39 0471 055 055",
                                #                 html.Br(),  
                                #                 " Fax: +39 0471 055 099",
                                #                 html.Br(), 
                                #                 " Email: ",
                                #                 html.A(
                                #                     href = "mailto:daniele.antonucci@eurac.edu",
                                #                     children = "daniele.antonucci@eurac.edu"
                                #                 )
                                #             ]
                                #         )
                                #     ]
                                # )
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
                    # id="footer_middle_up",
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
                                                                    href="/contact",
                                                                ),
                                                                html.A(
                                                                    className="navispecial_link linkstyle linkstyle__1",
                                                                    href = "/contact",
                                                                    title="Contact",
                                                                    # **{'itemprop':'url'},
                                                                    children=[
                                                                        html.Span(
                                                                            "Contact",
                                                                            # **{'itemprop':'name'},
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