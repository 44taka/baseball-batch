from loguru import logger
from bs4 import BeautifulSoup
import fire
import requests


def test():
    logger.debug('debug!!')
    r = requests.get('https://www.yakult-swallows.co.jp/game/schedule/2022/9')
    print(r)

    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.find_all('title'))
    print('test')


if __name__ == '__main__':
    fire.Fire(test)
