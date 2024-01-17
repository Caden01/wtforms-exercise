from flask import Flask, render_template, redirect, url_for
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SECRET_KEY"] = "asdfjjlkf3w3fwlkj"

connect_db(app)
with app.app_context():
    db.create_all()


@app.route("/")
def pets_list():
    """Show list of pets"""

    pets = Pet.query.all()
    return render_template("pets_list.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Allow user to add a pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        pet_info = {k: v for k, v in form.data.items()}
        print(pet_info)
        new_pet = Pet(
            name = pet_info["name"],
            species = pet_info["species"],
            photo_url = pet_info["photo"],
            age = pet_info["age"],
            notes = pet_info["notes"]
        )

        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for("pets_list"))
    else:
        return render_template("add_pet_form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Allow user to edit pet info"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        pet.photo_url = form.photo.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect(url_for("pets_list"))

    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)
        