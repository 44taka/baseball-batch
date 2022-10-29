from datetime import datetime
from pydantic import BaseModel, validator


class TeamModel(BaseModel):
    id: int
    league_kbn: int
    team_name: str
    yahoo_team_id: int
    is_deleted: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    """
    以下よりビジネスロジック内でのバリデーションを定義
    """
    @validator('league_kbn')
    def check_league_kbn(cls, v):
        if v not in [1, 2]:
            raise ValueError('league_kbn は 1 か 2 を指定してください。')
        return v

    @validator('team_name')
    def check_team_name_max_length(cls, v):
        if len(v) > 50:
            raise ValueError('team_name は50文字以内で入力してください。')
        return v

    @validator('is_deleted')
    def check_zero_or_one(cls, v):
        if v not in [0, 1]:
            raise ValueError('is_deleted は 0 か 1 を指定してください。')
        return v
