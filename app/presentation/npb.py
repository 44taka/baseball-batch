from loguru import logger

from domain.repository.team import ITeamRepository
from domain.repository.scraping import IScrapingRepository
from domain.repository.scoreboard import IScoreboardRepository


class NpbPresentation(object):
    def __init__(self, sr: IScrapingRepository, tr: ITeamRepository, sbr: IScoreboardRepository):
        self._sr = sr
        self._tr = tr
        self._sbr = sbr

    async def run(self, team_id: int, url: str) -> int:
        try:
            # team_idのバリデーション
            team = self._tr.find_by_id(team_id=team_id)
            # チーム情報取得
            teams = self._tr.find_all()
            # スクレピング実行
            data = self._sr.scrape(
                team_id=team.id, teams=teams, url=url.format(team.code)
            )
            for datum in data:
                if self._sbr.find(data=datum):
                    self._sbr.update(data=datum)
                else:
                    self._sbr.insert(data=datum)
            return 0
        except Exception as e:
            logger.exception(e)
            return 1
