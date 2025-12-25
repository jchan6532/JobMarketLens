from __future__ import annotations
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.db.models.job_posting import JobPosting
from app.nlp.role_classifier import classify_role

BATCH_SIZE = 500

def backfill_role_category(db: Session) -> int:
    updated = 0

    q = db.query(JobPosting).yield_per(BATCH_SIZE)
    for job in q:
        role = classify_role(job.title, job.description)
        if role and job.role_category != role:
            job.role_category = role
            updated += 1

    db.commit()
    return updated

def main() -> None:
    db = SessionLocal()
    try:
        n = backfill_role_category(db)
        print(f"Updated {n} job_postings.role_category")
    finally:
        db.close()

if __name__ == "__main__":
    main()
