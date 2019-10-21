from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User


class LoginForm(FlaskForm):
    username = StringField('User name', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class': 'form-control'})
    remember_me = BooleanField('Remember me', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Sign in', render_kw={'class': 'btn btn-primary'})


class RegistrationForm(FlaskForm):
    username = StringField('User name', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password2 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')], render_kw={'class': 'form-control'})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'class': 'form-control'})
    submit = SubmitField('Sign in', render_kw={'class': 'btn btn-primary'})

    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError('Username exists')

    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError('Email exists')
