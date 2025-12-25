from pydantic import BaseModel
from datetime import date

class CityCount(BaseModel):
    city: str
    count: int


class RoleCount(BaseModel):
    role_category: str
    count: int


class SkillCount(BaseModel):
    slug: str
    name: str
    category: str
    count: int

class SkillTrendPoint(BaseModel):
    # First day of the month
    period_start: date
    count: int