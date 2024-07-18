from flask import Flask
from .views import product_bp


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object('config.Config')

    app.register_blueprint(product_bp)

    return app