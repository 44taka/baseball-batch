from typing import List

from bs4 import BeautifulSoup
import requests

from domain.repository.scraping import IScrapingRepository
from domain.model.win_loss import WinLossModel


class SwallowsScraping(IScrapingRepository):
    def scrape(self, url: str) -> List[WinLossModel]:
        # スクレイピング準備
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        data = []
        for element in soup.select('section.unit-month div.wrapper .item-schedule'):
            # href属性ないものはスキップ
            if not element.has_attr('href'):
                continue
            # ゲームステータス判定
            game_status = 0
            if element.select_one('.i-game-cate').text == 'JERA セ・リーグ公式戦':
                game_status = 1
            # 試合日
            game_date = element.select_one('.t-calendar-date-day time').attrs['datetime'].split('T')[0]
            # 勝敗、引き分けフラグ判定用
            score_mark = element.select_one('.t-calendar-score-mark img').attrs['alt']
            # リストに追加
            data.append(
                WinLossModel(
                    date=game_date,
                    game_status=game_status,
                    is_win=1 if score_mark == '◯' else 0,
                    is_lose=1 if score_mark == '●' else 0,
                    is_draw=1 if score_mark == '△' else 0,
                    team_id=1
                )
            )
        return data











