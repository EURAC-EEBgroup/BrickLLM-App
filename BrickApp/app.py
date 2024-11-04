import dash
from dash import dcc, html, Dash
import dash_mantine_components as dmc
import os
import webview
from dash import Dash, DiskcacheManager, CeleryManager, Input, Output, html, callback
import celery
from components.footer import Footer, footer_2, footer_1
from components.sidebar import Sidebar
from dash_iconify import DashIconify
from flask import Flask 


# dash mantine components >= 14.0.1 requires React 18+
dash._dash_renderer._set_react_version("18.2.0")
# server = Flask(__name__, root_path=DASH_RELATIVE_PATH)
 
if 'REDIS_URL_BROKER' in os.environ:
    # Use Redis & Celery if REDIS_URL set as an env variable
    from celery import Celery
    celery_app = Celery(__name__, broker=os.environ['REDIS_URL_BROKER'], backend=os.environ['REDIS_URL_BACKEND'])
    background_callback_manager = CeleryManager(celery_app)
 
else:
    # Diskcache for non-production apps when developing locally
    import diskcache
    cache = diskcache.Cache("./cache")
    background_callback_manager = DiskcacheManager(cache)
 

app = Dash(
    __name__, 
    use_pages=True,
    # server=server,
    assets_folder='assets',  
    title="Brick-LLM",
    suppress_callback_exceptions=True,
    background_callback_manager=background_callback_manager,
    external_stylesheets=dmc.styles.ALL,
    # requests_pathname_prefix='/brick_llm/'
)


server = app.server
server.config.update(
    SECRET_KEY=os.environ.get('SECRET_KEY', os.urandom(12)),
)

from components.header import Header
from components.drawer import Drawer

from callbacks import (callback_header, callback_settings, callback_home)

dynamic_background = html.Iframe(
    id="iframe_background_image",
    src="/assets/world-map.html",
    style={
        "position": "fixed",  # Makes the iframe act as a background
        "top": 0,
        "left": 0,
        "bottom": 0,
        "right": 0,
        "width": "100%",
        "height": "100%",
        "overflow": "hidden",  # Hides both x and y overflow
        "border": "none"  # Removes the border around the iframe
    }
)

app.layout = dmc.MantineProvider(
    id="mantine-provider",
    forceColorScheme='light',
    children=[
        dmc.NotificationProvider(position="top-center",autoClose=False, w='60%'),
        html.Div(id="notifications-container"),
        dcc.Location(id='url_app'),
        dcc.Store(id='color-theme', storage_type='session'),
        dcc.Store(id='log-output-store', data=""),
        dcc.Store(id='log-progress-store', data=""),
        dcc.Store(id='ttl-result', data={}),
        dmc.AppShell(
            header={"height": 80},
            children=[
                Header,
                Drawer,
                dmc.AppShellMain(
                    [
                        dynamic_background,
                        dash.page_container
                    ]
                    
                ),
                # footer_2,
                # footer_1,
                Footer,
                # Sidebar
            ],
            padding="xl",
            aside={
                "width": 300,
                "breakpoint": "xl",
                "collapsed": {"desktop": False, "mobile": True},
            },
        )
    ]
)

def run_native_dash_app(dash_app: Dash, window_title: str = None) -> None:
    """Run dash app as native web app
    Use PyWebView to run a dash app as a native web app
      * install with `pip install pywebview`
      * project home page: https://pywebview.flowrl.com/
      * github: https://github.com/r0x0r/pywebview
        * Actively developed as of 2022-04-27 (checked on 2022-06-27)
    :param dash_app: a dash app with server and title attributes
    :param window_title: title for app window; use None if `dash_app.title` should be used
    :return: None
    >>> app = Dash('Native Dash App Demo')
    >>> app.layout = html.Div(['App Layout'])
    >>> run_native_dash_app(app)
    """
    if window_title is None:
        window_title = dash_app.title

    webview.create_window(window_title, dash_app.server)
    webview.start(debug=True)


if __name__ == '__main__':
    '''Run Dash application (Development)'''
    app.run_server(debug=True, port=8091, dev_tools_hot_reload=True)
    # app.run(debug=False) # uncomment this line to run Dash application, and comment otherwise.

    '''Run Pywebview application (Production)'''
    # run_native_dash_app(app) # uncomment this line to run Pywebview application, and comment otherwise.