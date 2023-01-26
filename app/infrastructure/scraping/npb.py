from typing import List
import datetime

from bs4 import BeautifulSoup
from loguru import logger
import requests

from domain.repository.scraping import IScrapingRepository
from domain.model.scoreboard import ScoreboardModel
from domain.model.team import TeamModel


class NpbScraping(IScrapingRepository):
    def scrape(self, team_id: int, teams: List[TeamModel], url: str) -> List[ScoreboardModel]:
        try:
            # TODO: SSL署名周りでエラーが起きるので暫定処理
            # https://stackoverflow.com/questions/66689696/urllib3-error-ssl-wrong-signature-type
            requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'DEFAULT@SECLEVEL=1'
            response = requests.get(url)
            response.encoding = 'utf-8'
        except Exception as e:
            logger.error(e)
            raise

        # スクレピング
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []
        try:
            # 年を取得
            year = soup.select_one('#tedivtitle td.tenamesubtitle h2').text[:4]
            month = None
            for element in soup.select('#tedivmaintbl table.terhdtbl tr.terlist'):
                # 試合がない日はスキップ
                if not element.select_one('td.termmdd'):
                    continue
                # tdのelement格納
                td = element.select('td')
                # 月日取得
                day = td[0].text
                if '/' in td[0].text:
                    month, day = td[0].text.split('/')
                # 対戦チームID取得
                vs_team_id = None
                for team in teams:
                    if team.short_name == td[1].text.replace('　', ''):
                        vs_team_id = team.id
                        break
                # スコア(得点、失点)取得
                runs_scored, runs_allowed = td[6].text.split('-')
                # データ格納
                data.append(
                    ScoreboardModel(
                        date=datetime.date(int(year), int(month), int(day)),
                        team_id=team_id,
                        vs_team_id=vs_team_id,
                        win=1 if td[7].text == '○' else 0,
                        lose=1 if td[7].text == '●' else 0,
                        draw=1 if td[7].text == '△' else 0,
                        runs_scored=int(runs_scored),
                        runs_allowed=int(runs_allowed),
                        is_deleted=0,
                        rank=int(td[10].text),
                    )
                )
            return data
        except Exception as e:
            logger.error(e)
            raise
