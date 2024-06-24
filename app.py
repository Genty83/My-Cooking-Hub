"""
 Main app file: Contains all the flask funcionality 
for running the application 
"""

# IMPORTS
import os
from flask import (render_template, session, url_for,
    flash, redirect, request
    )
from bson.objectid import ObjectId
from src import app





# Home page
@app.route("/")
def home():
    return render_template("home.html")


# View My Recipes page
@app.route("/view_my_recipes")
def view_my_recipes():
    return render_template("view_my_recipes.html")


# Create New Recipes page
@app.route("/create_new_recipe")
def create_new_recipe():
    return render_template("create_new_recipe.html")



if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP"),
        port = int(os.environ.get("PORT")),
        debug = os.environ.get("DEBUG")
    )