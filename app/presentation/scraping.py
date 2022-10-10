from domain.usecase.scraping import IScrapingUseCase


class ScrapingPresentation(object):
    def __init__(self, su: IScrapingUseCase):
        self._su = su

    def run(self, url) -> int:
        try:
            self._su.scrape(url=url)
            return 0
        except:
            return 1
