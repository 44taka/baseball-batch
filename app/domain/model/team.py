from datetime import datetime
from pydantic import BaseModel, validator


class TeamModel(BaseModel):
    id: int
    league_kbn: int
    code: str
    name: str
    short_name: str
    color_cd: str
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

    @validator('code')
    def check_code_max_length(cls, v):
        if len(v) > 2:
            raise ValueError('code は2文字以内で入力してください。')
        return v

    @validator('name')
    def check_name_max_length(cls, v):
        if len(v) > 50:
            raise ValueError('team_name は50文字以内で入力してください。')
        return v

    @validator('short_name')
    def check_short_name_max_length(cls, v):
        if len(v) > 10:
            raise ValueError('short_name は50文字以内で入力してください。')
        return v

    @validator('color')
    def check_color_max_length(cls, v):
        if len(v) > 10:
            raise ValueError('color は50文字以内で入力してください。')
        return v

    @validator('is_deleted')
    def check_zero_or_one(cls, v):
        if v not in [0, 1]:
            raise ValueError('is_deleted は 0 か 1 を指定してください。')
        return v
