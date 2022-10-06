from domain.repository.scraping import IScrapingRepository
from domain.repository.win_loss import IWinLossRepository
from domain.usecase.scraping import IScrapingUseCase


class ScrapingUseCase(IScrapingUseCase):
    def __init__(self, sp: IScrapingRepository, wlr: IWinLossRepository):
        self._sp = sp
        self._wlr = wlr

    def scrape(self, url):
        # TODO: エラーハンドリングしっかり
        data = self._sp.scrape(url=url)
        for datum in data:
            self._wlr.save(data=datum)
        return data
