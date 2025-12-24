from __future__ import annotations
from sqlalchemy.orm import Session

from app.db.models.job_posting import JobPosting
from app.db.models.job_skill import JobSkill
from app.nlp.skill_extractor import extract_skills

def backfill_job_skills(db: Session, slug_to_id: dict[str, int]) -> int:
    """
    For each job posting, extract skills and insert into job_skills.
    Returns number of new JobSkill rows inserted.
    """
    inserted = 0

    jobs = db.query(JobPosting.id, JobPosting.description).all()

    for job_id, desc in jobs:
        slugs = extract_skills(desc or "")
        if not slugs:
            continue

        skill_ids = [slug_to_id[s] for s in slugs if s in slug_to_id]
        if not skill_ids:
            continue

        # find existing pairs for this job
        existing_skill_ids = {
            sid for (sid,) in db.query(JobSkill.skill_id).filter(JobSkill.job_id == job_id).all()
        }

        new_rows = [
            JobSkill(job_id=job_id, skill_id=sid)
            for sid in skill_ids
            if sid not in existing_skill_ids
        ]

        if new_rows:
            db.add_all(new_rows)
            inserted += len(new_rows)

    db.commit()
    return inserted
