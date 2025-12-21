from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class CanonicalJob:
    title: str
    company: str
    description: str
    city: str
    province: str
    country: str
    posted_date: date | None
    salary_raw: str | None
    source_name: str
    source_job_id: str