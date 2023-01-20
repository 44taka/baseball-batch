from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, validator


class ScoreboardModel(BaseModel):
    id: Optional[int]
    date: date
    team_id: int
    vs_team_id: int
    win: int = 0
    lose: int = 0
    draw: int = 0
    runs_scored: int
    is_deleted: int
    runs_allowed: int
    rank: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    """
    以下よりビジネスロジック内でのバリデーションを定義
    """
    # @validator('game_status')
    # def check_game_status(cls, v):
    #     if v not in [0, 1, 2, 3]:
    #         raise ValueError('input 0 or 1 or 2 or 3.')
    #     return v
    #
    # @validator('is_win', 'is_lose', 'is_draw', 'is_deleted')
    # def check_zero_or_one(cls, v):
    #     if v not in [0, 1]:
    #         raise ValueError('input 0 or 1.')
    #     return v
