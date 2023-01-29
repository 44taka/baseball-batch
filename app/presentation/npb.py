from loguru import logger

# from domain.repository.team import ITeamRepository
# from domain.repository.scraping import IScrapingRepository
# from domain.repository.scoreboard import IScoreboardRepository

from domain.usecase.npb import INpbUseCase


class NpbPresentation(object):
    def __init__(self, nu: INpbUseCase):
        self._nu = nu

    async def run(self, team_id: int, url: str) -> bool:
        result = self._nu.register(team_id=team_id, url=url)
        return True

        # # team_idのバリデーション
        # team = self._tr.find_by_id(team_id=team_id)
        # # チーム情報取得
        # teams = self._tr.find_all()
        # # スクレピング実行
        # logger.info(f'team: {team.name}, url: {url.format(team.code)}')
        # data = self._sr.scrape(
        #     team_id=team.id, teams=teams, url=url.format(team.code)
        # )
        # for datum in data:
        #     if self._sbr.find(data=datum):
        #         self._sbr.update(data=datum)
        #     else:
        #         self._sbr.insert(data=datum)
        # return True

        # try:
        #     # team_idのバリデーション
        #     team = self._tr.find_by_id(team_id=team_id)
        #     # チーム情報取得
        #     teams = self._tr.find_all()
        #     # スクレピング実行
        #     logger.info(f'team: {team.name}, url: {url.format(team.code)}')
        #     data = self._sr.scrape(
        #         team_id=team.id, teams=teams, url=url.format(team.code)
        #     )
        #     for datum in data:
        #         if self._sbr.find(data=datum):
        #             self._sbr.update(data=datum)
        #         else:
        #             self._sbr.insert(data=datum)
        #     return True
        # except Exception as e:
        #     # logger.error(e)
        #     raise e
        #     # return 1
