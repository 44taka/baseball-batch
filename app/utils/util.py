from typing import List
import datetime
import urllib.parse

from configs.database import DatabaseConfig
from configs.batch import BatchEnvConfig


class Util(object):

    @staticmethod
    def parse_url_path(url: str, i: int) -> str:
        parsed = urllib.parse.urlparse(url=url)
        return parsed.path.split('/')[i]

    @staticmethod
    def get_query_param(url: str, key: str) -> str:
        queries = urllib.parse.urlparse(url).query
        return urllib.parse.parse_qs(queries)[key][0]

    @staticmethod
    def get_date_list(begin_date: datetime.date, end_date: datetime.date) -> List[datetime.date]:
        return [
            begin_date + datetime.timedelta(i) for i in range((end_date - begin_date).days + 1)
        ]

    @staticmethod
    def is_in_period(target_date: datetime.date, from_date: datetime.date, to_date: datetime.date) -> bool:
        return from_date <= target_date <= to_date

    @staticmethod
    def get_database_config_dict(database_config: DatabaseConfig, batch_env_config: BatchEnvConfig) -> dict:
        database_config_dict = database_config.dict()
        if batch_env_config.env != 'production':
            del database_config_dict['ssl']
        return database_config_dict
