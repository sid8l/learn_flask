from flask import abort, Blueprint, render_template, current_app

from webapp.news.models import News
from webapp.weather import weather_by_city

blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    title = 'News hoho'
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    news_lists = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()
    return render_template('news/index.html', page_title=title, weather=weather, news_lists=news_lists)


@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()
    if not my_news:
        abort(404)

    return render_template('news/single_news.html', page_title=my_news.title, news=my_news)
