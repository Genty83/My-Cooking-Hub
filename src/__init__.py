# IMPORTS
import os
from flask import Flask

# Create instance of the app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")