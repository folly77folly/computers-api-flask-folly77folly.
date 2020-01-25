from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import app, db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    price = db.Column(db.Integer, nullable=False)
    ram_size = db.Column(db.Integer, nullable=False)
    disk_size  = db.Column(db.Integer, nullable=False)
    qty = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Company %r>' %self.name

    def __init__(self, name, price, ram_size, disk_size, qty):
        self.name = name
        self.price = price
        self.ram_size = ram_size
        self.disk_size = disk_size
        self.qty = qty
