from datetime import date, datetime
from pydantic import BaseModel, validator


class ScheduleModel(BaseModel):
    id: int
    schedule_kbn: int
    start_date: date
    end_date: date
    is_deleted: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    """
    以下よりビジネスロジック内でのバリデーションを定義
    """
    @validator('schedule_kbn')
    def check_schedule_kbn(cls, v):
        if v not in [1, 2]:
            raise ValueError('schedule_kbn は 1 か 2 を指定してください。')
        return v

    @validator('end_date')
    def check_date_terms(cls, v, values, **kwargs):
        if 'start_date' in values and v <= values['start_date']:
            raise ValueError('start_date must input past date.')
        return v

    @validator('is_deleted')
    def check_zero_or_one(cls, v):
        if v not in [0, 1]:
            raise ValueError('is_deleted は 0 か 1 を指定してください。')
        return v
