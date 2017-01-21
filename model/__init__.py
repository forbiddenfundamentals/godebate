from app import app
from mongoengine import *

connection = connect(app.config['DB_NAME'])
