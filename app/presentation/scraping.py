from domain.usecase.scraping import IScrapingUseCase


class ScrapingPresentation(object):
    def __init__(self, su: IScrapingUseCase):
        self._su = su

    def run(self, url):
        result = self._su.scrape(url=url)
        return result
