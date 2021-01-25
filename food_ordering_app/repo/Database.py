from flask_pymongo import PyMongo
from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()

APP = Flask(__name__)

APP.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME')
APP.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(APP)
