import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return '<img src="https://flask.palletsprojects.com/en/3.0.x/_static/flask-vertical.png">'
    
    from . import ods
    app.register_blueprint(ods.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app