from dataclasses import dataclass
from app.ingestion.types.SalaryRange import SalaryRange
from app.ingestion.types.CanonicalJob import CanonicalJob

@dataclass(frozen=True)
class NormalizedJob:
    canonical_job: CanonicalJob

    # Derived fields
    title_clean: str
    company_clean: str
    city_clean: str
    province_clean: str

    salary_range: SalaryRange
