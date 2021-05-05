from datetime import datetime
from app import app
from extensions import db

class QueueM(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(201), nullable = True)
    firstname = db.Column(db.String(201), nullable = True)
    number = db.Column(db.Integer())
    email = db.Column(db.String(120), unique=True, nullable=False)
    date = db.Column(db.String(201), nullable = True)
    oclock = db.Column(db.Integer())
    delete_number = db.Column(db.Integer())


    def __repr__ (self):
        return self.name

    def __init__ (self, name, firstname, number, email, date, oclock, delete_number):
        self.name = name
        self.firstname = firstname
        self.number = number
        self.email = email
        self.date = date
        self.oclock = oclock
        self.delete_number = delete_number


    def save(self):
        db.session.add(self)
        db.session.commit()