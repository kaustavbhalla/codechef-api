from datetime import date
from pydantic import BaseModel, Field
from typing import Optional

class Contest(BaseModel):
    contestCode: Optional[str] = None
    name: str = Field(...)
    startDate: date
