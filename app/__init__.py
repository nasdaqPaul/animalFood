from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    db.init_app(app)

    from app.main import main
    from app.admin import admin
    from app.web_api import web_api
    with app.app_context():
        app.register_blueprint(main)
        app.register_blueprint(admin)
        app.register_blueprint(web_api)
        db.create_all()

        return app
