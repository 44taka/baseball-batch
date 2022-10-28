from urllib.parse import urlparse
from typing import List
import datetime


class Util(object):

    @staticmethod
    def parse_url_path(url: str, i: int) -> str:
        parsed = urlparse(url=url)
        return parsed.path.split('/')[i]

    @staticmethod
    def get_date_list(begin_date: datetime.date, end_date: datetime.date) -> List[datetime.date]:
        return [
            begin_date + datetime.timedelta(i) for i in range((end_date - begin_date).days + 1)
        ]
