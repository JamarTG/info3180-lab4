from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
class UploadForm(FlaskForm):
    file = FileField('Upload Image', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    