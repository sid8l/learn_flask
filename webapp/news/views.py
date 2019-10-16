from flask import Blueprint, render_template, current_app

from webapp.news.models import News
from webapp.weather import weather_by_city

blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    title = 'News hoho'
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    news_lists = News.query.order_by(News.published.desc()).all()
    return render_template('index.html', page_title=title, weather=weather, news_lists=news_lists)
