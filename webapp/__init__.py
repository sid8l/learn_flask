from flask import Flask, render_template

from webapp.weather import weather_by_city
from webapp.python_org_news import get_python_news


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = 'News hoho'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_lists = get_python_news()
        return render_template('index.html', page_title=title, weather=weather, news_lists=news_lists)
    return app