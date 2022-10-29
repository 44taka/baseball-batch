from typing import List
import datetime

from bs4 import BeautifulSoup
from loguru import logger
import requests

from domain.repository.scraping import IScrapingRepository
from domain.model.win_loss import WinLossModel
from utils.util import Util


class YahooScraping(IScrapingRepository):
    def scrape(self, team_id: int, url: str) -> List[WinLossModel]:
        logger.info('scrape url: ' + url)
        try:
            response = requests.get(url)
        except Exception as e:
            logger.exception(e)
            raise

        # 月、年の文字列取得
        year_str, month_str = Util.get_query_param(url, 'month').split('-')

        # スクレピング
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
        try:
            for element in soup.select(
                    '#tm_clnd .bb-calendarTable__row .bb-calendarTable__data .bb-calendarTable__wrap'
            ):
                # 試合がない日はスキップ
                if not element.select_one('.bb-calendarTable__versusTeam'):
                    continue

                # レギュラーシーズン以外はスキップ
                game_date = datetime.date(
                    int(year_str), int(month_str), int(element.select_one('.bb-calendarTable__date').text)
                )
                if not Util.is_in_period(
                    target_date=game_date, from_date=datetime.date(2022, 3, 25),  to_date=datetime.date(2022, 10, 3)
                ):
                    continue

                # 試合終了以外はスキップ
                if element.select_one('.bb-calendarTable__status').text != '試合終了':
                    continue

                # ゲームステータス判定
                game_status = 1
                # 交流戦判定
                if Util.is_in_period(
                    target_date=game_date, from_date=datetime.date(2022, 5, 24), to_date=datetime.date(2022, 6, 16)
                ):
                    game_status = 2

                # リストに追加
                data.append(
                    WinLossModel(
                        date=game_date,
                        game_status=game_status,
                        is_win=1 if element.select_one('.bb-calendarTable__score .bb-calendarTable__win') else 0,
                        is_lose=1 if element.select_one('.bb-calendarTable__score .bb-calendarTable__lose') else 0,
                        is_draw=1 if element.select_one('.bb-calendarTable__score .bb-calendarTable__draw') else 0,
                        team_id=team_id
                    )
                )
            return data
        except Exception as e:
            logger.exception(e)
            raise
