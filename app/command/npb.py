import sys
import time
import random

from loguru import logger
from orator import DatabaseManager

from utils.util import Util
from configs.batch import BatchEnvConfig
from configs.database import DatabaseConfig
from infrastructure.scraping.npb import NpbScraping
from infrastructure.persistence.team import TeamPersistence
from infrastructure.persistence.scoreboard import ScoreboardPersistence
from presentation.npb import NpbPresentation


class NpbCommand(object):

    def run(self, team_id: int) -> None:
        logger.info('start npb!!')
        urls = [
            'https://npb.jp/bis/teams/results_{}_04.html',
            'https://npb.jp/bis/teams/results_{}_05.html',
            'https://npb.jp/bis/teams/results_{}_06.html',
            'https://npb.jp/bis/teams/results_{}_07.html',
            'https://npb.jp/bis/teams/results_{}_08.html',
            'https://npb.jp/bis/teams/results_{}_09.html',
            'https://npb.jp/bis/teams/results_{}_10.html',
        ]
        # DB準備
        db_config = Util.get_database_config_dict(
            database_config=DatabaseConfig(), batch_env_config=BatchEnvConfig()
        )
        db = DatabaseManager(config={'mysql': db_config})

        # 処理準備
        team_persistence = TeamPersistence(db=db)
        scoreboard_persistence = ScoreboardPersistence(db=db)
        scraping = NpbScraping()
        presentation = NpbPresentation(sr=scraping, tr=team_persistence, sbr=scoreboard_persistence)

        # 処理開始
        status = 0
        for url in urls:
            logger.info('scrape status: processing...')
            status = presentation.run(team_id=team_id, url=url)
            if status != 0:
                break
            time.sleep(random.randint(1, 3))

        logger.info('end npb!!')
        sys.exit(status)
