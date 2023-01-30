from time import time
import asyncio

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
        begin_time = time()

        # 設定ファイル準備
        batch_config = BatchConfig()
        # DB接続準備
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

        # 処理開始
        task_results = []
        try:
            # 非同期で処理を行う
            async with asyncio.TaskGroup() as tg:
                task1 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_april, delay=0))
                task2 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_may, delay=0))
                task3 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_june, delay=0))
                task4 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_july, delay=1))
                task5 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_august, delay=1))
                task6 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_september, delay=1))
                task7 = tg.create_task(npb_presentation.run(team_id=team_id, url=batch_config.url_october, delay=1))
            task_results.extend([
                f'{task1.result()=}', f'{task2.result()=}', f'{task3.result()=}',
                f'{task4.result()=}', f'{task5.result()=}', f'{task6.result()=}',
                f'{task7.result()=}'
            ])
        except* Exception as e:
            logger.error(e.exceptions)

        # 各タスクのステータス格納
        task_status = [
            f'{task1._state=}', f'{task2._state=}', f'{task3._state=}', f'{task4._state=}',
            f'{task5._state=}', f'{task6._state=}', f'{task7._state=}',
        ]
        logger.info('-----------------------------------------------------------')
        logger.info('END - NPB\'s Website is scraping.')
        logger.info(f'process time: {str(time() - begin_time)} seconds.')
        logger.info(f'task results: {task_results=}')
        logger.info(f'task status: {task_status=}')
        logger.info('-----------------------------------------------------------')
