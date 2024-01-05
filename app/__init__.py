from flask import Flask, g


def create_app():
    app = Flask(__name__)

    from app.routes import bp

    app.register_blueprint(bp, url_prefix="/")

    return app