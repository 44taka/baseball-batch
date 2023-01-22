from pydantic import BaseSettings


class BatchConfig(BaseSettings):
    env: str
    url_april: str
    url_may: str
    url_june: str
    url_july: str
    url_august: str
    url_september: str
    url_october: str

    class Config:
        env_file_encoding = 'utf-8'
        env_prefix = 'batch_'
