from typing import Optional, Required
from pydantic import BaseModel
from enum import Enum

class typeOfUser(str, Enum):
    Student = "Student"
    Professional = "Professional"
    Other = "Other"


class User(BaseModel):
    name: str
    userName: str
    country: Optional[str]
    typeOf: typeOfUser
    institution: Optional[str]
    rating: Optional[int]
    division: Optional[str]
    stars: Optional[int] = 0
    globalRank: Optional[int]
    countryRank: Optional[int]
    contestsParticipated: Optional[int] = 0
