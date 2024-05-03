from app import app
from models import db, Pet

app.app_context().push()

db.drop_all()
db.create_all()

p = Pet(name="Jane", species="dog", age="Young",
        photo_url="https://images.rawpixel.com/image_png_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvcHUyMzMxNzg4LWltYWdlLXJtNTAzLTAxXzEtbDBqOXFyYzMucG5n.png")
db.session.add(p)

p2 = Pet(name="Blob", species="cat", age="Old", available=False)
db.session.add(p2)
db.session.commit()
