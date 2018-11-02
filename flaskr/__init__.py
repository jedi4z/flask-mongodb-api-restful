from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from .env import env
    env.init_app(app)

    from .mongo import mongo
    mongo.init_app(app)

    from .endpoints import api
    api.init_app(app)

    return app
