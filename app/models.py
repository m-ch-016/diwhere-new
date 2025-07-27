from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    price = db.Column(db.String(50))
    image = db.Column(db.String(500))
    link = db.Column(db.String(500), unique=True, index=True)
    source = db.Column(db.String(100))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name, 
            'price': self.price, 
            'image': self.image, 
            'link': self.link, 
            'source': self.source,
        }

