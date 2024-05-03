from app import app
from models import db, User

app.app_context().push()

db.drop_all()
db.create_all()

u = User(name="Jane", email="jane@jane.com")
db.session.add(u)
db.session.commit()
