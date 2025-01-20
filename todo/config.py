import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:Oluwayemi2002..,@localhost:5432/TodoAppFlask')
    SQLALCHEMY_TRACK_MODIFICATIONS = False