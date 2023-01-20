from typing import List

from loguru import logger

from domain.repository.scraping import IScrapingRepository
from domain.repository.win_loss import IWinLossRepository
from domain.repository.team import ITeamRepository
from domain.usecase.scraping import IScrapingUseCase
from domain.model.team import TeamModel


class NpbUseCase(IScrapingUseCase):
    def __init__(self, sp: IScrapingRepository, wlr: IWinLossRepository, tr: ITeamRepository):
        self._sp = sp
        self._wlr = wlr
        self._tr = tr

    def scrape(self, team_id: int, teams: List[TeamModel], url: str) -> int:
        try:
            team = self._tr.find_by_id(team_id=team_id)
            logger.debug('team name: ' + team.team_name)
            for datum in self._sp.scrape(team_id=team.id, teams=teams, url=url.format(str(team.cd))):
                self._wlr.save(data=datum)
            return 0
        except Exception:
            raise
