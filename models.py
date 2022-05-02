from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    # Return a printable value
    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.username,
            'email': self.email
        }

class Food(db.Model):
    __tablename__ = 'food'
    
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(), nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    days_before = db.Column(db.Integer)

    def __init__(self, creator_id, created, name, expiration_date):
        self.creator_id = creator_id
        self.created = created
        self.name = name
        self.expiration_date = expiration_date
        self.days_before = days_before


    # Return a printable value
    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'creator_id': self.creator_id,
            'created': self.created,
            'name': self.name,
            'expiration_date': self.expiration_date,
            'days_before': self.days_before
        }