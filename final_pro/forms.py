from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from .route import User


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    user_type = SelectField("User Type", choices=[('', 'Select User Type'), ('Customer', 'Customer'),
                                                  ("Agent", "Agent")], validators=[DataRequired()])
    zip_code = StringField("Zip Code", validators=[DataRequired()])
    address = TextAreaField("Address", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exist in our system, please try another one')


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Login')

