import json
import re

import bs4

from Book import Book


def parsing(s: str):
    out = ''

    soup = bs4.BeautifulSoup(s, 'html.parser')
    books = soup.find_all('li', class_='book-item__item book-item--full')
    for book in books:
        try:
            title = book.find_all('a', class_='book-item__title')[0].text
        except (IndexError, AttributeError):
            title = ''
        try:
            author = book.find('a', class_='book-item__author').text
        except (IndexError, AttributeError):
            author = ''

        book_item_editions = book.find_all('table', class_='book-item-edition')
        for book_item in book_item_editions:
            isbn = ''
            lang = ''
            year = ''
            for row in book_item.find_all('tr'):
                try:
                    k = row.find_all('td')[0].text
                    v = row.find_all('td')[1].text
                    if k == 'Язык:':
                        lang = v
                    if k == 'ISBN:':
                        isbn = v
                    if k == 'Год издания:':
                        year = v
                except AttributeError:
                    continue

        rating = book.find_all('div', class_='book-item__rating')[0].text
        try:
            total_read = str(book.find_all('div', class_='book-item-stat')[0].find('a').get('title', default=''))
            total_read = re.sub(r'[^\d]', '', total_read)
        except (TypeError, IndexError, AttributeError) as e:
            total_read = ''
        book = Book(title, author, year, isbn, rating, total_read)

        out += str(book)
        out += '\n'
    return out


def str_x_to_dict(s: str) -> dict:
    s = bytes(s, 'UTF-8')
    s = s.decode('unicode-escape').encode('latin1').decode('utf-8')
    d = json.loads(s)
    return d


def read_html_file(file_name: str):
    try:
        with open(file_name, encoding='utf-8') as f:
            s = f.read()
            return s
    except FileNotFoundError:
        return ''
