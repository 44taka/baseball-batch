from typing import List
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from loguru import logger
import requests

from domain.repository.scraping import IScrapingRepository
from domain.model.win_loss import WinLossModel
from utils.util import Util


class FightersScraping(IScrapingRepository):
    def scrape(self, team_id: int, url: str) -> List[WinLossModel]:
        try:
            response = requests.get(url)
        except Exception as e:
            logger.exception(e)
            raise

        parse_date = Util.parse_url_path(url, 3)

        # スクレピング
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
        try:
            for element in soup.select('#pl_contentInner table.pl_gameCalendar02 tbody tr'):
                # 勝敗取得
                win_loss = element.select_one('td:nth-child(4) img')
                if win_loss is None:
                    continue
                # ゲームステータス判定
                exibition_title = element.select_one('td:nth-child(2) p.pl_exibitionTitle')
                game_status = 0
                if exibition_title is None:
                    game_status = 1
                elif exibition_title.text == 'セ・パ交流戦':
                    game_status = 2
                # 試合日
                game_day = element.select_one('td:nth-child(1) div.pl_date p:nth-child(1) nobr').text
                # リストに追加
                data.append(
                    WinLossModel(
                        date=parse_date[:4] + '-' + parse_date[4:6] + '-' + game_day,
                        game_status=game_status,
                        is_win=1 if win_loss.attrs['alt'] == 'win' else 0,
                        is_lose=1 if win_loss.attrs['alt'] == 'lost' else 0,
                        is_draw=1 if win_loss.attrs['alt'] == 'drow' else 0,
                        team_id=team_id
                    )
                )
            return data
        except Exception as e:
            logger.exception(e)
            raise
