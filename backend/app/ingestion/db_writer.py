from __future__ import annotations
from typing import Iterable
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from app.db.models.job_posting import JobPosting
from app.ingestion.types.NormalizedJob import NormalizedJob


def upsert_job_posting(db: Session, normalized_job: NormalizedJob) -> None:
    """
    Upsert into job_postings using (source_name, source_job_id) unique constraint.
    """
    canonical_job = normalized_job.canonical_job

    statement = insert(JobPosting).values(
        title=canonical_job.title,
        company=canonical_job.company,
        description=canonical_job.description,
        city=canonical_job.city,
        province=canonical_job.province,
        country=canonical_job.country,
        posted_date=canonical_job.posted_date,
        role_category=None,

        salary_min=normalized_job.salary_range.salary_min,
        salary_max=normalized_job.salary_range.salary_max,
        salary_raw=canonical_job.salary_raw,

        source_name=canonical_job.source_name,
        source_job_id=canonical_job.source_job_id,
    )

    statement = statement.on_conflict_do_update(
        constraint="uq_job_source",
        set_={
            "title": statement.excluded.title,
            "company": statement.excluded.company,
            "description": statement.excluded.description,
            "city": statement.excluded.city,
            "province": statement.excluded.province,
            "country": statement.excluded.country,
            "posted_date": statement.excluded.posted_date,
            "salary_min": statement.excluded.salary_min,
            "salary_max": statement.excluded.salary_max,
            "salary_raw": statement.excluded.salary_raw,
        },
        where=(
            (JobPosting.title != statement.excluded.title) |
            (JobPosting.company != statement.excluded.company) |
            (JobPosting.description != statement.excluded.description) |
            (JobPosting.city != statement.excluded.city) |
            (JobPosting.province != statement.excluded.province) |
            (JobPosting.posted_date != statement.excluded.posted_date) |
            (JobPosting.salary_min != statement.excluded.salary_min) |
            (JobPosting.salary_max != statement.excluded.salary_max) |
            (JobPosting.salary_raw != statement.excluded.salary_raw)
        )
    )

    db.execute(statement)

def upsert_job_postings(db: Session, jobs: Iterable[NormalizedJob], commit_every: int = 500) -> int:
    """
    Batch upsert. Returns number of processed rows.
    """
    count = 0
    for nj in jobs:
        upsert_job_posting(db, nj)
        count += 1

        if count % commit_every == 0:
            db.commit()

    db.commit()
    return count
