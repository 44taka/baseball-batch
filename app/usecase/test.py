from domain.repository.team import ITeamRepository
from domain.usecase.test import ITestUseCase

from infrastructure.scraping.swallows import SwallowsScraping


class TestUseCase(ITestUseCase):
    def __init__(self, tp: ITeamRepository):
        self._tp = tp

    def find_all(self):
        scp = SwallowsScraping()
        scp.scrape('https://www.yakult-swallows.co.jp/game/schedule/2022/9')
        result = self._tp.find_all()
        return result
