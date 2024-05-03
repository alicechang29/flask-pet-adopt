import os

from flask import Flask, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, User
from forms import AddSnackForm, UserForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgresql:///flask_wtforms")
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
db.init_app(app)

app.config["SECRET_KEY"] = "oh-so-secret"
debug = DebugToolbarExtension(app)


@app.get("/")
def homepage():
    """Show homepage links."""

    return render_template("index.jinja")


@app.route("/add", methods=["GET", "POST"])
def add_snack():
    """Snack add form; handle adding."""

    form = AddSnackForm()

    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        # do stuff with data/insert to db

        flash(f"Added {name} at {price}")
        return redirect("/add")

    else:
        return render_template(
            "snack_add_form.jinja", form=form)


@app.route("/users/<int:uid>/edit", methods=["GET", "POST"])
def edit_user(uid):
    """Show user edit form and handle edit."""

    user = db.get_or_404(User, uid)
    form = UserForm(obj=user)

    if form.validate_on_submit():
        user.name = form.name.data
        user.email = form.email.data
        db.session.commit()
        flash(f"User {uid} updated!")
        return redirect(f"/users/{uid}/edit")

    else:
        return render_template("user_form.jinja", form=form)
