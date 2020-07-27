# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv

# -- Initialization section --
app = Flask(__name__)

# first let's load environment variables in .env
# load_dotenv()

# then store environment variables with new names 
# MONGO_USER = os.getenv("MONGO_USER")
# MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

# name of database
# app.config['MONGO_DBNAME'] = 'test'

# URI of database - replace with your information 
# app.config['MONGO_URI'] = f'mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@cluster0-7bt79.mongodb.net/test?retryWrites=true&w=majority'


mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')
def index():
    # collection = mongo.db.events
    # events = collection.find({})
    return render_template('index.html', events = events)