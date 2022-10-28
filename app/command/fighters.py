import sys
import time
import random

from loguru import logger

from configs.database import db
from infrastructure.scraping.fighters import FightersScraping
from infrastructure.persistence.win_loss import WinLossPersistence
from infrastructure.persistence.team import TeamPersistence
from usecase.scraping import ScrapingUseCase
from presentation.scraping import ScrapingPresentation


class FightersCommand(object):

    def run(self) -> None:
        logger.info('start fighters scraping.')
        # 動的にする
        urls = [
            'https://www.fighters.co.jp/game/schedule/202203/index.html',
            'https://www.fighters.co.jp/game/schedule/202204/index.html',
            'https://www.fighters.co.jp/game/schedule/202205/index.html',
            'https://www.fighters.co.jp/game/schedule/202206/index.html',
            'https://www.fighters.co.jp/game/schedule/202207/index.html',
            'https://www.fighters.co.jp/game/schedule/202208/index.html',
            'https://www.fighters.co.jp/game/schedule/202209/index.html',
            'https://www.fighters.co.jp/game/schedule/202210/index.html',
        ]

        # 処理準備
        win_loss_persistence = WinLossPersistence(db=db)
        team_persistence = TeamPersistence(db=db)
        fighters_scraping = FightersScraping()
        fighters_usecase = ScrapingUseCase(
            sp=fighters_scraping, wlr=win_loss_persistence, tr=team_persistence
        )
        swallows_presentation = ScrapingPresentation(su=fighters_usecase)

        # 処理開始
        status = 0
        for url in urls:
            logger.info('scrape url: ' + url)
            logger.info('scrape status: processing...')
            status = swallows_presentation.run(
                team_id=11,
                url=url
            )
            time.sleep(random.randint(1, 3))
        logger.info('end fighters scraping.')
        sys.exit(status)
