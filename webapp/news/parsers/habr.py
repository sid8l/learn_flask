from datetime import datetime

from bs4 import BeautifulSoup

from webapp.news.parsers.utils import save_news, get_html


def get_habr_snippets():
    html = get_html('https://habr.com/en/search/?target_type=posts&order_by=date&q=python&flow=')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='content-list_posts').findAll('li', class_='content-list__item_post')
        # print(all_news)
        for news in all_news:
            title = news.find('a', class_='post__title_link').text
            url = news.find('a', class_='post__title_link')['href']
            published = news.find('span', class_='post__time').text
            print(title, url, published)
            # try:
            #     published = datetime.strptime(published, '%Y-%m-%d')
            # except ValueError:
            #     published = datetime.now()
            # save_news(title=title, url=url, published=published)
