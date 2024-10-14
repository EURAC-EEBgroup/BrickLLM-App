import dash_mantine_components as dmc
from dash import html

Footer =  dmc.AppShellFooter(
    h=30,
    withBorder=True,
    children=[
        dmc.Container(
            children=[
                html.Div(
                    [
                        dmc.Text(
                            html.A(
                                "Copyright © Eurac Research",
                                href="http://www.eurac.edu/en/pages/default.aspx",
                                style={
                                    "color": "#CC3425",
                                }
                            ),
                            style={
                                "textAlign": "center"
                            }
                        ),
                    ]
                )
            ],
            style={
                "maxWidth":"600px",
                "paddingLeft": "24px",
                "paddingRight": "24px",
                "display": "flex",
                "flexDirection": "column"
            }
        )
    ],
    style={
        "paddding": ["24px", "16px"],
        "backgroundColor": "#eeeeee"
    }
)

footer_2 = html.Div(
    # id="footer_grey",
    className="section_footer",
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

