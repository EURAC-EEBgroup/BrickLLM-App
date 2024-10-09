import dash
from dash import dcc, html, Dash
import dash_mantine_components as dmc
import os
import webview
from dash import Dash, DiskcacheManager, CeleryManager, Input, Output, html, callback
import celery


# dash mantine components >= 14.0.1 requires React 18+
dash._dash_renderer._set_react_version("18.2.0")
 
if 'REDIS_URL' in os.environ:
    # Use Redis & Celery if REDIS_URL set as an env variable
    from celery import Celery
    celery_app = Celery(__name__, broker=os.environ['REDIS_URL'], backend=os.environ['REDIS_URL'])
    background_callback_manager = CeleryManager(celery_app)
 
else:
    # Diskcache for non-production apps when developing locally
    import diskcache
    cache = diskcache.Cache("./cache")
    background_callback_manager = DiskcacheManager(cache)
 

app = Dash(
    __name__, 
    use_pages=True,
    assets_folder='assets',  
    title="Brick LLM",
    suppress_callback_exceptions=True,
    background_callback_manager=background_callback_manager
    # external_stylesheets=dmc.styles.ALL,
)

server = app.server
server.config.update(
    SECRET_KEY=os.environ.get('SECRET_KEY', os.urandom(12)),
)

from components.header import Header
from components.drawer import Drawer

from callbacks import (callback_header, callback_settings, callback_home)

app.layout = dmc.MantineProvider(
    id="mantine-provider",
    forceColorScheme='dark',
    children=[
        dmc.NotificationProvider(),
        html.Div(id='notifiaction-wrap'),
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
                    dash.page_container
                ),
            ],
            padding="xl",
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
    app.run_server(debug=False, port=8092, dev_tools_hot_reload=True)
    # app.run(debug=False) # uncomment this line to run Dash application, and comment otherwise.

    '''Run Pywebview application (Production)'''
    # run_native_dash_app(app) # uncomment this line to run Pywebview application, and comment otherwise.