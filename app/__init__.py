from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
app = Flask(__name__)
#Session(app)
app.config['SECRET_KEY'] = "b/[prlfmq=e-cmsrt"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nenhoxkimuxxle:63215cc022e181d2b073bbce4dd6ce276597437e20886e3d33685e7520b8a118@ec2-18-235-97-230.compute-1.amazonaws.com:5432/d4gs4tqc9rv7el'
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user:password@localhost/database"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)

from app import views
