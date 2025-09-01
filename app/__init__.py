from flask import Flask
from .main import pages_bp

def create_app(debug=True):
    app = Flask(__name__)
    app.debug = debug

    app.register_blueprint(pages_bp)

    return app
