from flask import Flask
from os import environ
from project.config import Production, Development, Database
from flask_sqlalchemy import SQLAlchemy
# from . import views


#initialize the app

app = Flask(__name__)

#Choosing production or development mode 

app.config.from_object(Development)

#setting controllers for database connection

app.config.from_object(Database)

#initialize database

db = SQLAlchemy(app)

#bringing all views to be served
# import views