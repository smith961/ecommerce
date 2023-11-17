from flask_sqlalchemy import SQLAlchemy;
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    companyName = db.Column(db.String)

    def __repr__(self):
        return f'<User{self.name}>'
    
class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)


class Cart(db.Model, SerializerMixin):
    __tablename__ = 'carts'

    id=db.Column(db.Integer, primary_key = True)
    # product_id =
    # user_id = 