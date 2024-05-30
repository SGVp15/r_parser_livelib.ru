import os

START_GAME = 3  # с какого номера скачать
END_GAME = 3  # по какой включительно

COLUMNS_EXCEL = ['player_id', 'team_id', 'match_id']  # колонки, которые нужно включить в CSV

DOWNLOAD_SITES = False  # Скачивать сайты True/False
DELETE_HTML_FILES = False  # Удалять сайты True/False

url_base = 'https://www.livelib.ru/genre/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B0%D1%8F-%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%82%D1%83%D1%80%D0%B0/best/listview/biglist/~'

data = './data'
HTML_DIR = os.path.join(data, 'html')

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(data, exist_ok=True)

EXPORT_CSV_FILE = os.path.join(data, 'End.csv')
