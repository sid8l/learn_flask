from webapp import create_app
from webapp.python_org_news import get_python_news
from webapp.news.parsers.habr import get_habr_snippets

app = create_app()
with app.app_context():
    get_habr_snippets()
