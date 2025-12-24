from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class CanonicalJob:
    title: str
    company: str | None
    description: str | None
    city: str | None
    province: str | None
    country: str | None
    posted_date: date | None
    salary_raw: str | None
    source_name: str
    source_job_id: str