from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

env_config = os.getenv("APP_SETTINGS", "config.Config")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import NetworkDevices


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()