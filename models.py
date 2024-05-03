"""Demo file showing off a model for SQLAlchemy."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
dbx = db.session.execute


class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.mapped_column(
        db.Integer,
        db.Identity(),
        primary_key=True,
    )

    name = db.mapped_column(
        db.String(50),
        nullable=False,
    )

    email = db.mapped_column(
        db.String(50),
        nullable=True,
    )
