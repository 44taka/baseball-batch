from loguru import logger

from domain.usecase.scraping import IScrapingUseCase


class ScrapingPresentation(object):
    def __init__(self, su: IScrapingUseCase):
        self._su = su

    def run(self, team_id: int, url: str) -> int:
        try:
            self._su.scrape(team_id=team_id, url=url)
            return 0
        except Exception as e:
            logger.exception(e)
            return 1
