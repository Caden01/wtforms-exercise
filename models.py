from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG = "https://images6.fanpop.com/image/photos/41500000/golden-retriever-puppy-cute-puppies-41528617-400-400.jpg"

class Pet(db.Model):
    """Pets available for adoption"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=DEFAULT_IMG)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

def connect_db(app):
    """Connect database to flask app"""

    db.app = app
    db.init_app(app)