from typing import List

from bs4 import BeautifulSoup
from loguru import logger
import requests

from domain.repository.scraping import IScrapingRepository
from domain.model.win_loss import WinLossModel


class SwallowsScraping(IScrapingRepository):
    def scrape(self, team_id: int, url: str) -> List[WinLossModel]:
        try:
            response = requests.get(url)
        except Exception as e:
            logger.exception(e)
            raise

        # スクレピング
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
        try:
            for element in soup.select('section.unit-month div.wrapper .item-schedule'):
                # href属性ないものはスキップ
                if not element.has_attr('href'):
                    continue
                # ゲームステータス判定
                game_status = 0
                if element.select_one('.i-game-cate').text == 'JERA セ・リーグ公式戦':
                    game_status = 1
                elif element.select_one('.i-game-cate').text == 'セ・パ交流戦':
                    game_status = 2
                # 試合日
                game_date = element.select_one('.t-calendar-date-day time')
                if game_date is None:
                    continue
                # 勝敗、引き分けフラグ判定用
                score_mark = element.select_one('.t-calendar-score-mark img')
                if score_mark is None:
                    continue
                # リストに追加
                data.append(
                    WinLossModel(
                        date=game_date.attrs['datetime'].split('T')[0],
                        game_status=game_status,
                        is_win=1 if score_mark.attrs['alt'] == '◯' else 0,
                        is_lose=1 if score_mark.attrs['alt'] == '●' else 0,
                        is_draw=1 if score_mark.attrs['alt'] == '△' else 0,
                        team_id=team_id
                    )
                )
            return data
        except Exception as e:
            logger.exception(e)
            raise
