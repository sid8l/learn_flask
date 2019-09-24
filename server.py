from flask import Flask, render_template

from weather import weather_by_city


app = Flask(__name__)


@app.route('/')
def index():
    title = 'Weather forecast'
    weather = weather_by_city('Minsk,Belarus')
    return render_template('index.html', page_title=title, weather=weather)


if __name__ == "__main__":
    app.run(debug=True)
