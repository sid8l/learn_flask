from datetime import datetime, timedelta
import locale
import platform

from bs4 import BeautifulSoup

from webapp.news.parsers.utils import save_news, get_html


if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, 'russian')
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


def parse_habr_date(date_str):
    if 'сегодня' in date_str:
        today = datetime.now()
        date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
    if 'вчера' in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str = date_str.replace('сегодня', yesterday.strftime('%d %B %Y'))
    try:
        return datetime.strptime(date_str, '%d %B %Y в %H:%M')
    except ValueError:
        return datetime.now()


def get_habr_snippets():
    html = get_html('https://habr.com/ru/search/?target_type=posts&q=python&order_by=date')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='content-list_posts').findAll('li', class_='content-list__item_post')
        # print(all_news)
        for news in all_news:
            title = news.find('a', class_='post__title_link').text
            url = news.find('a', class_='post__title_link')['href']
            published = news.find('span', class_='post__time').text
            published = parse_habr_date(published)
            save_news(title, url, published)
            # try:
            #     published = datetime.strptime(published, '%Y-%m-%d')
            # except ValueError:
            #     published = datetime.now()
            # save_news(title=title, url=url, published=published)
