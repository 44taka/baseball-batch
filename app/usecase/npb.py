from loguru import logger

from domain.repository.team import ITeamRepository
from domain.repository.scraping import IScrapingRepository
from domain.repository.scoreboard import IScoreboardRepository
from domain.usecase.npb import INpbUseCase


class NpbUseCase(INpbUseCase):
    def __init__(self, sr: IScrapingRepository, tr: ITeamRepository, sbr: IScoreboardRepository):
        self._sr = sr
        self._tr = tr
        self._sbr = sbr

    def register(self, team_id: int, url: str) -> None:
        try:
            # team_idのバリデーション
            team = self._tr.find_by_id(team_id=team_id)
            if team is None:
                raise ValueError('team_id not exist.')
            # チーム情報取得
            teams = self._tr.find_all()
            # スクレピング実行
            logger.info(f'team: {team.name}, url: {url.format(team.code)}')
            data = self._sr.scrape(
                team_id=team.id, teams=teams, url=url.format(team.code)
            )
            # データ登録
            for datum in data:
                if self._sbr.find(data=datum):
                    self._sbr.update(data=datum)
                else:
                    self._sbr.insert(data=datum)
        except ValueError as e:
            logger.error(f'code: E001, error: {e}')
            raise e
