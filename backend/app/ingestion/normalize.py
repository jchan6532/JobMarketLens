from app.ingestion.normalizers.salary import parse_salary
from app.ingestion.types.CanonicalJob import CanonicalJob
from app.ingestion.types.NormalizedJob import NormalizedJob

def _clean_lower(s: str | None) -> str | None:
    if not s:
        return None
    return _clean(s).lower()

def _clean_upper(s: str | None) -> str | None:
    if not s:
        return None
    return _clean(s).upper()

def _clean(s: str | None) -> str | None:
    if not s:
        return None
    return " ".join(s.split()).strip()

def normalize_job(job: CanonicalJob) -> NormalizedJob:
    salary_range = parse_salary(job.salary_raw)

    return NormalizedJob(
        canonical_job=job,
        title_clean=_clean(job.title),
        company_clean = _clean(job.company),
        city_clean = _clean_lower(job.city),
        province_clean = _clean_upper(job.province),
        salary_range=salary_range,
    )
