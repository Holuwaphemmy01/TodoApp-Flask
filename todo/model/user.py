from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    first_name = database.Column(database.String(80), nullable=False)
    last_name = database.Column(database.String(80), nullable=False)
    username = database.Column(database.String(80), unique=True, nullable=False)
    password = database.Column(database.String(120), nullable=False)