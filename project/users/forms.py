from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    username = StringField(label="username", validators=[InputRequired()])
    password = PasswordField(label="password", validators=[InputRequired()])
