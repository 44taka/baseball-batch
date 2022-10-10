import sys
import time
import random

from loguru import logger

from configs.database import db
from infrastructure.scraping.swallows import SwallowsScraping
from infrastructure.persistence.win_loss import WinLossPersistence
from infrastructure.persistence.team import TeamPersistence
from usecase.scraping import ScrapingUseCase
from presentation.scraping import ScrapingPresentation


class SwallowsCommand(object):

    def run(self) -> None:
        logger.info('start swallows scraping.')
        # 動的にする
        urls = [
            'https://www.yakult-swallows.co.jp/game/schedule/2022/3',
            'https://www.yakult-swallows.co.jp/game/schedule/2022/4',
            'https://www.yakult-swallows.co.jp/game/schedule/2022/5',
            'https://www.yakult-swallows.co.jp/game/schedule/2022/6',
            'https://www.yakult-swallows.co.jp/game/schedule/2022/7',
            'https://www.yakult-swallows.co.jp/game/schedule/2022/8',
            'https://www.yakult-swallows.co.jp/game/schedule/2022/9',
            'https://www.yakult-swallows.co.jp/game/schedule/2022/10',
        ]

        # 処理準備
        win_loss_persistence = WinLossPersistence(db=db)
        team_persistence = TeamPersistence(db=db)
        swallows_scraping = SwallowsScraping()
        swallows_usecase = ScrapingUseCase(
            sp=swallows_scraping, wlr=win_loss_persistence, tr=team_persistence
        )
        swallows_presentation = ScrapingPresentation(su=swallows_usecase)

        # 処理開始
        status = 0
        for url in urls:
            logger.info('scrape url: ' + url)
            logger.info('scrape status: processing...')
            status = swallows_presentation.run(
                url=url
            )
            time.sleep(random.randint(1, 3))
        logger.info('end swallows scraping.')
        sys.exit(status)
