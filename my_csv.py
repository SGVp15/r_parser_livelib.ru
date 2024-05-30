import csv
import os

from config import EXPORT_CSV_FILE, HTML_DIR, COLUMNS_EXCEL
from my_parser import parsing, read_html_file


def create_final_csv_file():
    html_files = [file for file in os.listdir(HTML_DIR) if file.endswith('.html')]
    with open(EXPORT_CSV_FILE, mode='w', encoding='utf-8', newline='') as f:
        for file in html_files:
            with open(os.path.join(HTML_DIR, file), mode='r', encoding='utf-8') as html_file:
                s = str(parsing(html_file.read()))
                f.write(s)


create_final_csv_file()
