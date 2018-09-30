from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkeythatonlyiknowandyoudontbecauseitssecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Wyatt/Flask/Trivia/finish/database.db'

db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class Games(UserMixin, db.Model):
