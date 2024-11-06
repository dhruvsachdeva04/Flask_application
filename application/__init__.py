import os
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

# Check if the variables are being set correctly
print("SECRET_KEY:", app.config["SECRET_KEY"])
print("MONGO_URI:", app.config["MONGO_URI"])

# Initialize MongoDB
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes
