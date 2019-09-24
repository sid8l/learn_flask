from flask import Flask, render_template

from weather import weather_by_city
from python_org_news import get_python_news


app = Flask(__name__)


@app.route('/')
def index():
    title = 'News hoho'
    weather = weather_by_city('Minsk,Belarus')
    news_lists = get_python_news()
    return render_template('index.html', page_title=title, weather=weather, news_lists=news_lists)


if __name__ == "__main__":
    app.run(debug=True)
