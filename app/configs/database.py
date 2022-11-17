# from orator import DatabaseManager
from pydantic import BaseSettings


class DatabaseCaConfig(BaseSettings):
    ca: str

    class Config:
        env_file_encoding = 'utf-8'
        env_prefix = 'mysql_'


class DatabaseConfig(BaseSettings):
    """DBの設定情報"""
    driver: str = 'mysql'
    host: str
    database: str
    user: str
    password: str
    prefix: str = ''
    ssl: DatabaseCaConfig = DatabaseCaConfig()

    class Config:
        env_file_encoding = 'utf-8'
        env_prefix = 'mysql_'
