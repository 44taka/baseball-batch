from orator import DatabaseManager
from pydantic import BaseSettings


class DatabaseConfig(BaseSettings):
    """DBの設定情報"""
    driver: str = 'mysql'
    host: str
    database: str
    user: str
    password: str
    prefix: str = ''

    class Config:
        env_file_encoding = 'utf-8'
        env_prefix = 'mysql_'


db_config = DatabaseConfig()
db = DatabaseManager(config={'mysql': db_config.dict()})
