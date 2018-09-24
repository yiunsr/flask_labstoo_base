

def init_app(app):
    from app.main import main
    app.register_blueprint(main, url_prefix='/')
