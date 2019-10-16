from getpass import getpass
import sys

from webapp import create_app
from webapp.db import db
from webapp.user.models import User


app = create_app()

with app.app_context():
    username = input('Input username: ')

    if User.query.filter(User.username == username).count():
        print('This username already exists.')
        sys.exit()

    password1 = getpass('Password: ')
    password2 = getpass('Password again: ')

    if not password1 == password2:
        print('passwords not matched')
        sys.exit()

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)
    db.session.add(new_user)
    db.session.commit()
    print(f'Create new user with id {new_user.id}')
