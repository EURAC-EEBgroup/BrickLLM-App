import dash
from dash import dcc, html, Dash
import dash_mantine_components as dmc
import os
from dash import Dash, DiskcacheManager, CeleryManager, html, callback

from components.footer import Footer

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
    assets_folder='assets',  
    title="Brick-LLM",
    suppress_callback_exceptions=True,
    background_callback_manager=background_callback_manager,
    external_stylesheets=dmc.styles.ALL,
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
                dash.page_container,
                Footer,
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

if __name__ == '__main__':
    '''Run Dash application (Development)'''
    app.run_server(debug=False, port=8091, dev_tools_hot_reload=False)
