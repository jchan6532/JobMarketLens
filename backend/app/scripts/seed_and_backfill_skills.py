from __future__ import annotations

from app.db.session import SessionLocal
from app.scripts.utils.seed_skills import seed_skills
from app.scripts.utils.backfill_job_skills import backfill_job_skills


def main() -> None:
    db = SessionLocal()
    try:
        inserted = seed_skills(db)
        print(f"Seeded {inserted} skills.")

        backfilled = backfill_job_skills(db=db, slug_to_id=inserted)
        print(f"Backfilled {backfilled} job_skills rows.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
