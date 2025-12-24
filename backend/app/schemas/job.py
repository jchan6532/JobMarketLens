from pydantic import BaseModel
from datetime import date

class JobResponse(BaseModel):
    model_config = {
        "from_attributes": True
    }

    id: int
    title: str
    company: str
    description: str
    city: str
    province: str
    country: str
    salary_min: int | None = None
    salary_max: int | None = None
    salary_raw: str | None = None
    posted_date: date | None = None
    role_category: str | None = None
    source_name: str
    source_job_id: str