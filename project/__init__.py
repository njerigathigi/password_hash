from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app = Flask(__name__)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///learn_auth.db"
app.config["SECRET_KEY"] = 'd46bda4c4a883757726e4793a6f5'
migrate = Migrate(app, db)
