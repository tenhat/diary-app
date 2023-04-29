from app import db
from sqlalchemy.orm import relationship

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    diaries = db.relationship('Diary', backref='author', lazy='dynamic')

class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tags = db.relationship('Tag', backref='diary', lazy='dynamic')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    diary_id = db.Column(db.Integer, db.ForeignKey('diary.id'))

    def __repr__(self):
        return f'<Tag {self.name}>'
