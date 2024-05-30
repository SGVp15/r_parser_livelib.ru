import asyncio
import os

import aiofiles
import aiohttp

from config import url_base, HTML_DIR, START_GAME, END_GAME, DOWNLOAD_SITES, DELETE_HTML_FILES
from my_csv import create_final_csv_file


async def download_sites(start, end):
    async with aiohttp.ClientSession() as session:
        for i in range(start, end + 1):
            url = url_base + str(i)
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.read()
                    async with aiofiles.open(os.path.join(HTML_DIR, f'{i}.html'), 'wb') as f:
                        await f.write(content)
                    print(f'Downloaded [ {i} ]')
                else:
                    print(f'Download [ {i} ]\t[Error]')


def del_files(start_game, end_game):
    for file_name in range(start_game, end_game + 1):
        try:
            os.remove(os.path.join(HTML_DIR, f'{file_name}.html'))
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    if DOWNLOAD_SITES:
        asyncio.run(download_sites(START_GAME, END_GAME))
    create_final_csv_file()
    if DELETE_HTML_FILES:
        del_files(START_GAME, END_GAME)
