from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://diary_user:diary_password@db/diary_app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import User, Diary, Tag
import routes

if __name__ == "__main__":
    app.run(host='0.0.0.0')
