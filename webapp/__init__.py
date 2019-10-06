from flask import Flask, render_template

from webapp.weather import weather_by_city
from webapp.model import db, News
from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = 'News hoho'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_lists = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=title, weather=weather, news_lists=news_lists)

    @app.route('/login')
    def login():
        title = 'Sign in'
        login_form=LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    return app