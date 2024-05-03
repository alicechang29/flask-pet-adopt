"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, AnyOf, URL


class AddPetForm(FlaskForm):
    """Form for adding  pets."""

    name = StringField("Pet Name")
    species = StringField(
        "Species",
        validators=[AnyOf(values=['cat', 'dog', 'porcupine'])]
    )
    photo_url = StringField(
        "Photo URL",
        validators=[
            URL(require_tld=False),
            Optional()]
    )
    age = SelectField("Age",
                      choices=[
                          ('baby', 'Baby'),
                          ('young', 'Young'),
                          ('adult', 'Adult'),
                          ('senior', 'Senior')
                      ],
                      validators=[AnyOf(values=[
                          'baby',
                          'young',
                          'adult',
                          'senior'
                      ])]
                      )
    notes = TextAreaField("Notes")
