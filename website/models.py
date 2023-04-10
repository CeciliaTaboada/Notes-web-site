from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Primary Key
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default = func.now())#This always takes the current time when object is created
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Foreign key relationship

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #Primary Key
    email = db.Column(db.String(150), unique=True) #Emails must be unique, no other user can have the same email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')