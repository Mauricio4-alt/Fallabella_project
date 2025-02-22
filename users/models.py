from config import db


class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(250),unique=True,nullable=False)
    email = db.Column(db.String(250),unique=True,nullable=False)
    password = db.Column(db.String(250),nullable=False)
