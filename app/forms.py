from flask_wtf import FlaskForm
from wtforms import validators
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, DataRequired
from wtforms.fields.html5 import EmailField

images = ['png', 'jpg', 'jpeg', 'gif','jpe']


class ProfileForm(FlaskForm):
    fname = StringField('First name', validators=[InputRequired()])
    lname = StringField('Last name', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    gender = SelectField('Sex', choices=[('Male', 'Male'), ('Female', 'Female')])
    photo = FileField('Profile Picture', validators=[FileRequired(),FileAllowed(images, 'Images only!')])
    
    biography = TextAreaField('Biography', [
        DataRequired()
        ])