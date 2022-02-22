from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import declarative_base
# Base = declarative_base()
db = SQLAlchemy()

# class VideoModel(db.Model):
#     __tablename__ = 'VideoModel'
#     id = db.Column(db.Integer, primary_key = True)
#     order_num = db.Column(db.Integer, nullable=False)
#     first_name = db.Column(db.String(50))
#     second_name = db.Column(db.String(50))
#     start = db.Column(db.Integer)
#     length = db.Column(db.Integer)
#     category = db.Column(db.String(10), 
#                         nullable=False, 
#                         default='Background')
#     quality = db.Column(db.String(10), 
#                         nullable=False, 
#                         default='Low')
#     encoded_name = db.Column(db.String(100))
#     video_url = db.Column(db.String(50), nullable=False)
#     video_embed = db.Column(db.String(150))
#     bucket_url = db.Column(db.String(200))

class User(db.Model):
    __tablename__ = 'users_info'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

# class User(db.Model):
#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(128), unique=True, nullable=False)
#     active = db.Column(db.Boolean(), default=True, nullable=False)

#     def __init__(self, email):
#         self.email = email