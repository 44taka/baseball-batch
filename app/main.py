from loguru import logger
from bs4 import BeautifulSoup
import fire
import requests
from pydantic import ValidationError
from configs.database import DatabaseConfig, db
from domain.model.win_loss import WinLossModel

from infrastructure.persistence.team import TeamPersistence
from usecase.test import TestUseCase
from presentation.test import TestPresentation

from command.test_command import TestCommand
from command.swallows import SwallowsCommand


def test():
    logger.debug('debug!!')

    # DI注入
    tp = TeamPersistence(db=db)
    tu = TestUseCase(tp=tp)
    tpre = TestPresentation(tu=tu)
    logger.debug(tpre.find())

    # r = requests.get('https://www.yakult-swallows.co.jp/game/schedule/2022/9')
    # print(r)
    # soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.find_all('title'))
    # print('test')
    # config = DatabaseConfig()
    # print(config.dict())
    # print(db)

    # try:
    #     model = WinLossModel(
    #         id=1,
    #         date='2022-09-30',
    #         game_status=9,
    #         is_win=9,
    #         is_lose=1,
    #         is_draw=1,
    #         is_deleted=0,
    #         team_id=123
    #     )
    #     print(model)
    # except ValidationError as e:
    #     print(e)


class Main(object):
    test = TestCommand
    swallows = SwallowsCommand


if __name__ == '__main__':
    # fire.Fire(test)
    fire.Fire(Main)
