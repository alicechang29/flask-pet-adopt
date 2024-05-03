"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import Optional, AnyOf, URL


class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Pet Name")

    species = StringField(  # make it a SelectField
        "Species",
        validators=[AnyOf(values=['cat', 'dog', 'porcupine'])]
    )

    photo_url = StringField(
        "Photo URL",
        validators=[
            URL(require_tld=False),  # should be true for prod
            Optional()
        ]
    )

    age = SelectField(
        "Age",
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')
        ],
        validators=[AnyOf(values=[  # don't need validators for select field
            'baby',
            'young',
            'adult',
            'senior'
        ])]
    )

    # add optional validator. if optional, consider character limits
    notes = TextAreaField("Notes")


class EditPetForm(FlaskForm):
    """Form for editing a pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[
            URL(require_tld=False),
            Optional()
        ]
    )

    # add optional validator. if optional, consider character limits
    notes = TextAreaField("Notes")

    available = BooleanField("Available")
