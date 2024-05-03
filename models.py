"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
dbx = db.session.execute


class Pet(db.Model):
    """A pet"""

    __tablename__ = "pets"

    id = db.mapped_column(
        db.Integer,
        db.Identity(),
        primary_key=True,
    )

    name = db.mapped_column(
        db.Text,  # String
        nullable=False,
    )

    species = db.mapped_column(
        db.Text,  # String
        nullable=False,
    )

    photo_url = db.mapped_column(
        db.Text,
        nullable=False,
        default='',
    )

    age = db.mapped_column(
        db.Text,  # String
        nullable=False
    )

    notes = db.mapped_column(
        db.Text,
    )

    available = db.mapped_column(
        db.Boolean,
        nullable=False,
        default=True,
    )
