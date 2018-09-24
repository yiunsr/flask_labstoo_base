from flask import Flask
from config import config
from config import assets
from config import urls


def create_app(config_name):
    app = Flask(
        __name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(config[config_name])
    assets.init_app(app)
    urls.init_app(app)
    return app
