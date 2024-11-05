from dash import html
import dash_mantine_components as dmc
import dash 
from dash_iconify import DashIconify
dash.register_page(__name__,path_template=f"/contact")

text = "The tool is designed to simplify the creation of ontological models (based on Brick Schema) for buildings, facilities, and monitoring and control systems, through the use of Large Language Models "

text_1 = "Please feel free to contact us with any potential suggestions, avenues for collaboration, etc. "



def page_text_layout(content):
    
    simple_row = html.Div(
        className="row",
        children = [
            html.Div(className="col-lg-2 col-md-0 sol-sm-0", children = ""),
            html.Div(
                className="col-lg-10 col-md-12 col-sm-12",
                children = content
            ),
            html.Div(className="col-lg-2 col-md-0 sol-sm-0", children = ""),
        ],
    )

    return simple_row

contact_us = dmc.Group(
    children = [
        DashIconify(icon="line-md:email-twotone", width=30),
        html.Div(
            className="heading heading__2",
            children = "Contact us",
        )
    ]
)

def email_contact(email, name_contact):
    email_group = dmc.Flex(
        children = [
            html.A(
                DashIconify(icon="streamline:send-email", width=25),
                href=f"mailto:{email}",
                style={'text-decoration': 'none'}
            ),
            html.H2(name_contact)
        ],
        justify="flex-start",
        gap="md",
        mt=3
    )

    return email_group

name_contact = html.Div(
    children = [
        
        html.Div(
            className="heading heading__3",
            children = [
                "TOOL, LIBRARY and LLM - Eurac research"
            ],
            style = {'color':'rgb(6, 157, 201)'}
        ),
        
        dmc.Stack(
            [ email_contact("daniele.antonucci@eurac.edu", "Daniele Antonucci"),
            email_contact("marco.perinit@eurac.edu", "Marco Perini"),
            email_contact("olga.somova@eurac.edu", "Olga Somova"),
            ]
        ),
        dmc.Divider(variant="solid", mt=10),
        html.Div(
            className="heading heading__3",
            children = [
                "LIBRARY AND LLM - POLITO"
            ],
            style = {'color':'rgb(6, 157, 201)'}
        ),
        dmc.Stack(
            [email_contact("rocco.giudice@polito.it", "Rocco Giudice"),
             ]
        )
    ]
)


layout_ = dmc.Container(
    mt=90, 
    children = [
        dmc.Text("Contact",id="text1", opacity=0.7, fw=700, c="black"),
        dmc.Title("BRICK - LLM", id="text2",lh=1.2, order=3, mt="xs", fw=900, c="black"),
        dmc.Divider(variant = "solid", size="lg", mt=20, color="grey", pt=20, pl=20, pr=20),
        dmc.Text(text, mb=5, mt=2, opacity=0.9),
        dmc.Text(text_1, mt=20, mb=20, opacity=0.9, fw=700),
        name_contact
    ]
)

def layout():
    return layout_
