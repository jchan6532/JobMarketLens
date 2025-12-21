from app.ingestion.normalizers.salary import parse_salary
from app.ingestion.types.CanonicalJob import CanonicalJob
from app.ingestion.types.NormalizedJob import NormalizedJob

def normalize_job(job: CanonicalJob) -> NormalizedJob:
    salary_range = parse_salary(job.salary_raw)

    return NormalizedJob(
        canonical=job,
        title_clean=" ".join(job.title.split()).strip(),
        company_clean=" ".join(job.company.split()).strip(),
        city_clean=job.city.strip(),
        province_clean=job.province.strip().upper(),
        salary_range=salary_range,
    )
