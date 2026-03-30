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
    country: Optional[str] = None
    typeOf: typeOfUser = typeOfUser.Other
    institution: Optional[str] = None
    rating: Optional[int] = 0
    division: Optional[str] = "Unrated"
    stars: Optional[int] = 0
    globalRank: Optional[int] = -1
    countryRank: Optional[int] = -1
    contestsParticipated: Optional[int] = 0
