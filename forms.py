from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class UserAddForm(FlaskForm):
    """Signup form."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])



class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class UpdateUserForm(FlaskForm):
    """Update user profile and preferences form."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    #base_city = SelectField('Select Base City:', remove_option=True, coerce=int)
    #occupation = SelectField('Select Occupation:', remove_option=True, coerce=int)

class DeleteUserForm(FlaskForm):
    """Delete user form."""
    password = PasswordField('Password', validators=[Length(min=6)])
