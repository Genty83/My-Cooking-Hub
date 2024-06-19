"""
 Main app file: Contains all the flask funcionality 
for running the application 
"""

# IMPORTS
import os
from flask import render_template
from src import app


# Home page
app.route("/")
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP"),
        port = int(os.environ.get("PORT")),
        debug = os.environ.get("DEBUG")
    )