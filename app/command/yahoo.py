import sys
import time
import random

from loguru import logger
from orator import DatabaseManager

from utils.util import Util
from configs.batch import BatchEnvConfig
from configs.database import DatabaseConfig
from infrastructure.scraping.yahoo import YahooScraping
from infrastructure.persistence.win_loss import WinLossPersistence
from infrastructure.persistence.team import TeamPersistence
from usecase.scraping import ScrapingUseCase
from presentation.scraping import ScrapingPresentation


class YahooCommand(object):

    def run(self, team_id: int) -> None:
        logger.info('start yahoo sports scraping.')
        urls = [
            'https://baseball.yahoo.co.jp/npb/teams/{}/schedule?month=2022-03',
            'https://baseball.yahoo.co.jp/npb/teams/{}/schedule?month=2022-04',
            'https://baseball.yahoo.co.jp/npb/teams/{}/schedule?month=2022-05',
            'https://baseball.yahoo.co.jp/npb/teams/{}/schedule?month=2022-06',
            'https://baseball.yahoo.co.jp/npb/teams/{}/schedule?month=2022-07',
            'https://baseball.yahoo.co.jp/npb/teams/{}/schedule?month=2022-08',
            'https://baseball.yahoo.co.jp/npb/teams/{}/schedule?month=2022-09',
            'https://baseball.yahoo.co.jp/npb/teams/{}/schedule?month=2022-10',
        ]

        # DB準備
        db_config = Util.get_database_config_dict(
            database_config=DatabaseConfig(), batch_env_config=BatchEnvConfig()
        )
        db = DatabaseManager(config={'mysql': db_config})

        # 処理準備
        win_loss_persistence = WinLossPersistence(db=db)
        team_persistence = TeamPersistence(db=db)
        scraping = YahooScraping()
        usecase = ScrapingUseCase(sp=scraping, wlr=win_loss_persistence, tr=team_persistence)
        presentation = ScrapingPresentation(su=usecase)

        # 処理開始
        status = 0
        for url in urls:
            logger.info('scrape status: processing...')
            status = presentation.run(team_id=team_id, url=url)
            if status != 0:
                break
            time.sleep(random.randint(1, 3))

        logger.info('end yahoo sports scraping.')
        sys.exit(status)
