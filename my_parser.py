import json
import re
import bs4
from bs4 import formatter


def parsing(s: str):
    out = ''

    soup = bs4.BeautifulSoup(s, 'html.parser')
    books = soup.find_all('li', class_='book-item__item book-item--full')
    for book in books:
        try:
            title = book.find_all_next('a', class_='book-item__title')[0].text
        except (IndexError, AttributeError):
            title = ''
        try:
            author = book.find('a', class_='book-item__author').text
        except (IndexError, AttributeError):
            author = ''

        isbn = ''
        lang = ''
        year = ''
        book_item_editions = book.find_all_next('table', class_='book-item-edition')
        for book_item in book_item_editions:
            val = book_item.find_all_next('td')[0]
            a = val.text
            print(val.text)
            # [0].find_next('td')
            if val.text == 'Язык:':
                lang = val.find_next('td').text
            if val.text == 'ISBN:':
                isbn = val.find_next('td').text
            if val.text == 'Год издания:':
                year = val.find_next('td').text

        rating = book.find_all_next('div', class_='book-item__rating')[0].text
        print(f'{title=},{author=},{rating=},{isbn=},{year=}')
        out += '\t'.join([title, author, rating, year])
        out +='\n'
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
