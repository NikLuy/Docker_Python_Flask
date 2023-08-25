from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint("main", __name__, static_folder="static",template_folder="templates" )

# Define the index route
@main.route("/")
def index():
    return render_template("index.html")

# Define the profile route
@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)