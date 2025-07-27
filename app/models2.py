from enum import unique
from flask_login import UserMixin
from operator import index

from traitlets import default
from app import db, login

@login.user_loader
def loadUser(id):
    return User.query.get(id)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    price = db.Column(db.String(50))
    image = db.Column(db.String(500))
    weblink = db.Column(db.String(500), unique=True, index=True)
    source = db.Column(db.String(100))
    clicks = db.Column(db.Integer, default=0, server_default='0')
    rating = db.Column(db.Integer, default=0, server_default='0')
    trending = db.relationship('Trending', backref='product', lazy=True)

    # def to_dict(self):
    #     return {
    #         'name': self.name, 
    #         'price': self.price, 
    #         'image': self.image, 
    #         'weblink': self.weblink, 
    #         'source': self.source, 
    #         'clicks': self.clicks, 
    #         'rating': self.rating 
    #     }


class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    date = db.Column(db.DateTime)
    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(200), unique=True, index=True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    phonenum = db.Column(db.String(200))

class Trending(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    