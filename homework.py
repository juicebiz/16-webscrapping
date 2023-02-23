import bs4
import requests
from fake_headers import Headers

WORDS = [
    "Apple",
    "ChatGPT",
    "HTTPS",
]

url = 'https://habr.com/ru/all/'
url_ru = 'https://habr.com'

if __name__ == '__main__':
    print(url)
    response = requests.get(url, headers=Headers(os="win", headers=False).generate())
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')

    articles = soup.find_all('article')
    for article in articles:
        preview = article.find(class_="article-formatted-body").text
        for word in WORDS:
            if word in preview:
                href = article.find(class_="tm-article-snippet__title-link").attrs['href']
                full_href = f"{url_ru}{href}"
                date = article.find(class_="tm-article-datetime-published").find('time').attrs['title']
                title = article.find('h2').find('span').text
                print(date, title, full_href)