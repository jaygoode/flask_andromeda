from flask import Flask
from .views import views
from .auth import auth
from flask_sqlalchemy import SQLAlchemy
from os import path
import os 
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "1234"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.abspath(DB_NAME)}"

    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    with app.app_context():
        create_db()

    return app
def create_db():
    if not os.path.exists('website/' + DB_NAME):
        try:
            db.create_all()
            print("CREATED")
        except Exception as e:
            print("Database creation failed:", str(e))
    else:
        print("Database already exists")



