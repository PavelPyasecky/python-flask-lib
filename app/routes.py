from flask import render_template
from . import app, db


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET"])
def index():
    return render_template(
        "index.html",
        title="Home",
    )
