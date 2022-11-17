from pydantic import BaseSettings


class BatchEnvConfig(BaseSettings):
    env: str

    class Config:
        env_file_encoding = 'utf-8'
        env_prefix = 'batch_'
