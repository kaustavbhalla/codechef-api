from pydantic import BaseModel, Field
from typing import Optional

class Contest(BaseModel):
    contest_code: str
    contest_name: str
    contest_start_date: str
    contest_end_date: str
    contest_start_date_iso: str
    contest_end_date_iso: str
    contest_duration: str
    distinct_users: int


class SkillTest(BaseModel):
    contest_code: str
    contest_name: str
    contest_start_date: str
    contest_end_date: str
    contest_start_date_iso: str
    contest_end_date_iso: str
    contest_duration: str
    problem_count: int
    distinct_users: int

class ContestListResponse(BaseModel):
    status: str
    message: str
    present_contests: list[Contest] = Field(default_factory=list)
    future_contests: list[Contest] = Field(default_factory=list)
    past_contests: list[Contest] = Field(default_factory=list)
    practice_contests: list[Contest] = Field(default_factory=list)
    skill_tests: list[SkillTest] = Field(default_factory=list)
