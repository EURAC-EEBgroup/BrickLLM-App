import dash
from dash import html, dcc
import  dash_mantine_components as dmc
from dash_iconify import DashIconify


dash.register_page(__name__, path='/terms_condition')

layout_ = dmc.Container()

def layout():
    return layout_
