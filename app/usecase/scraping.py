from domain.repository.scraping import IScrapingRepository
from domain.repository.win_loss import IWinLossRepository
from domain.repository.team import ITeamRepository
from domain.usecase.scraping import IScrapingUseCase


class ScrapingUseCase(IScrapingUseCase):
    def __init__(self,
                 sp: IScrapingRepository,
                 wlr: IWinLossRepository,
                 tr: ITeamRepository
                 ):
        self._sp = sp
        self._wlr = wlr
        self._tr = tr

    def scrape(self, team_id: int, url: str) -> int:
        team = self._tr.find_by_id(team_id=team_id)
        for datum in self._sp.scrape(team_id=team.id, url=url):
            self._wlr.save(data=datum)
        return 0
