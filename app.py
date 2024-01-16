from flask import Flask, render_template, redirect
from models import db, connect_db, Pet

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresq:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)
db.create_all()


@app.route("/")
def pets_list():
    """Show list of pets"""

    pets = Pet.query.all()
    return render_template("pets_list.html", pets=pets)