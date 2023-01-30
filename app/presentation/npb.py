import asyncio
from loguru import logger
from domain.usecase.npb import INpbUseCase


class NpbPresentation(object):
    def __init__(self, nu: INpbUseCase):
        self._nu = nu

    async def run(self, team_id: int, url: str, delay: int) -> str:
        try:
            await asyncio.sleep(delay)
            self._nu.register(team_id=team_id, url=url)
            return 'Success'
        except asyncio.CancelledError as e:
            logger.info(f'task cancel: {team_id=}, {url=}')
            raise e
        except Exception as e:
            raise e
