from configs.database import db
from infrastructure.scraping.swallows import SwallowsScraping
from infrastructure.persistence.win_loss import WinLossPersistence
from usecase.scraping import ScrapingUseCase
from presentation.scraping import ScrapingPresentation


class SwallowsCommand(object):

    def run(self):
        win_loss_persistence = WinLossPersistence(db=db)
        swallows_scraping = SwallowsScraping()
        # TODO: ここでDIコンテナ使うのかな？
        swallows_usecase = ScrapingUseCase(sp=swallows_scraping, wlr=win_loss_persistence)
        swallows_presentation = ScrapingPresentation(su=swallows_usecase)
        swallows_presentation.run(
            url='https://www.yakult-swallows.co.jp/game/schedule/2022/9'
        )
