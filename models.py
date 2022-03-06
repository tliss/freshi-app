from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Returna printable value
    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.username
        }

class Post(db.Model):
    __tablename__ = 'post'
    
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(), nullable=False)
    body = db.Column(db.String(), nullable=False)

    def __init__(self, author_id, created, title, body):
        self.author_id = author_id
        self.created = created
        self.title = title
        self.body = body


    # Return a printable value
    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'author_id': self.author_id,
            'created': self.created,
            'title': self.title,
            'body': self.body
        }

class Food(db.Model):
    __tablename__ = 'food'
    
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    name = db.Column(db.String(), nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, creator_id, created, name, expiration_date):
        self.creator_id = creator_id
        self.created = created
        self.name = name
        self.expiration_date = expiration_date


    # Return a printable value
    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'creator_id': self.creator_id,
            'created': self.created,
            'name': self.name,
            'expiration_date': self.expiration_date
        }