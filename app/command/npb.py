from time import time
import asyncio
import sys

from loguru import logger
from orator import DatabaseManager

from utils.util import Util
from configs.batch import BatchConfig
from configs.database import DatabaseConfig
from infrastructure.scraping.npb import NpbScraping
from infrastructure.persistence.team import TeamPersistence
from infrastructure.persistence.scoreboard import ScoreboardPersistence
from presentation.npb import NpbPresentation

from usecase.npb import NpbUseCase


class NpbCommand(object):

    async def run(self, team_id: int) -> None:
        logger.info('-----------------------------------------------------------')
        logger.info(f'BEGIN - NPB\'s Website is scraping.')
        logger.info('-----------------------------------------------------------')
        # 設定ファイル準備
        begin_time = time()
        batch_config = BatchConfig()
        db_config = Util.get_database_config_dict(
            database_config=DatabaseConfig(), batch_config=batch_config
        )
        db = DatabaseManager(config={'mysql': db_config})

        # 処理準備
        team_persistence = TeamPersistence(db=db)
        scoreboard_persistence = ScoreboardPersistence(db=db)
        npb_scraping = NpbScraping()
        npb_usecase = NpbUseCase(sr=npb_scraping, tr=team_persistence, sbr=scoreboard_persistence)
        npb_presentation = NpbPresentation(nu=npb_usecase)
        # scraping = NpbScraping()
        #
        # presentation = NpbPresentation(sr=scraping, tr=team_persistence, sbr=scoreboard_persistence)

        # 処理開始
        status = 0
        # 非同期処理で並行処理を行う
        try:
            async with asyncio.TaskGroup() as tg:
                # TODO: エラーハンドリングを組み込むこと
                task1 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_april))
                task2 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_may))
                task3 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_june))
                task4 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_july))
                task5 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_august))
                task6 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_september))
                task7 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_october))
        except* Exception as e:
            logger.error('Error!!')
            logger.error(e.exceptions)
            # print(f"{e.exceptions=}")

        logger.info('-----------------------------------------------------------')
        logger.info('END - NPB\'s Website is scraping.')
        logger.info(f'process time: {str(time() - begin_time)} seconds.')
        logger.info('-----------------------------------------------------------')
        sys.exit(status)
