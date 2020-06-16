from wtforms import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from wtforms import HiddenField

import email_validator

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('This field must be empty!')

class CommentForm(Form):
    user = StringField('username', [
        validators.Required(message='The username is required!'),
        validators.length(min=4, max=20, message='Please enter a valid username.')
    ])
    email = EmailField('email', [
        validators.Required(message='This field is required!'),
        validators.Email()
    ])
    comment = TextField('Comment', [
        validators.Required(message='Please fill out this field!'),
        validators.length(min=20, max=100, message='Please send us min 20 characters, maximum 100')
    ])
    honeypot = HiddenField('', [
        length_honeypot
    ])