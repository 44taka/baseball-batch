from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class WinLossDepositModel(BaseModel):
    id: Optional[int]
    date: date
    deposit: int
    team_id: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
