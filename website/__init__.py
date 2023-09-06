from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "1234"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.abspath(DB_NAME)}"

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    with app.app_context():
        create_db()

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_db():
    if not os.path.exists("website/" + DB_NAME):
        try:
            db.create_all()
            print("CREATED")
        except Exception as e:
            print("Database creation failed:", str(e))
    else:
        print("Database already exists")
