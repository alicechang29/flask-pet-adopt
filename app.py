"""Flask app for adopt app."""

import os

from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.exceptions import NotFound  # TODO: what is this?

from models import db, dbx, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['SECRET_KEY'] = "secret"
db.init_app(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_homepage():
    """Display the pet adoption homepage"""

    q = db.select(Pet).where(Pet.available == "True")
    avail_pets = dbx(q).scalars().all()
    q = db.select(Pet).where(Pet.available == "False")
    unavail_pets = dbx(q).scalars().all()

    return render_template(
        "index.jinja",
        avail_pets=avail_pets,
        unavail_pets=unavail_pets
    )


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Shows add pet form and adds a pet to DB"""

    form = AddPetForm()

    if form.validate_on_submit():
        pet = Pet()
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data

        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template(
            "add_pet_form.jinja",
            form=form
        )


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Shows edit pet form and allows for edits"""

    pet = db.get_or_404(Pet, pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect("/")

    else:
        return render_template(
            "edit_pet_form.jinja",
            form=form,
            pet=pet
        )
