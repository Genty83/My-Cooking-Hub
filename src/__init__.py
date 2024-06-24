# IMPORTS
import os
from flask import Flask
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env


# Create instance of the app
app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")

mongo = PyMongo(app)

