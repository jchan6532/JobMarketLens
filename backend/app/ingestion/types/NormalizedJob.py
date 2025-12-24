from dataclasses import dataclass
from app.ingestion.types.SalaryRange import SalaryRange
from app.ingestion.types.CanonicalJob import CanonicalJob

@dataclass(frozen=True)
class NormalizedJob:
    canonical_job: CanonicalJob

    # Derived fields
    title_clean: str
    company_clean: str | None
    city_clean: str | None
    province_clean: str | None

    salary_range: SalaryRange
