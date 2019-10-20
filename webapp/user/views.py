from flask import render_template, Blueprint, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user

from webapp import db
from webapp.user.models import User
from webapp.user.forms import LoginForm, RegistrationForm


blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = 'Sign in'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(f'Hello {user.username}')
            return redirect(url_for('news.index'))
    flash('Wrong username or password')
    return redirect(url_for('user.login'))


@blueprint.route('/registration')
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = 'Sign up'
    registration_form = RegistrationForm()
    return render_template('user/registration.html', page_title=title, form=registration_form)


@blueprint.route('/registration-login', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Successful registration')
        return redirect(url_for('user.login'))
    flash('Please fill all correctly')
    return redirect(url_for('user.registration'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Logout')
    return redirect(url_for('news.index'))
