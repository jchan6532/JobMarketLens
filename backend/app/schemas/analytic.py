from pydantic import BaseModel

class CityCount(BaseModel):
    city: str
    count: int


class RoleCount(BaseModel):
    role_category: str
    count: int