# models.py
from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)  
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Person {self.first_name} {self.last_name}>'
