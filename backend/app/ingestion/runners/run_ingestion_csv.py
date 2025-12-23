from __future__ import annotations
import argparse
from pathlib import Path
from sqlalchemy.orm import Session

from app.ingestion.loaders.csv_loader import load_jobs_csv
from app.ingestion.normalize import normalize_job
from app.ingestion.db_writer import upsert_job_postings
from app.db.session import SessionLocal
from app.ingestion.config import ADAPTERS, CSV_DATA_DIR

def run_ingestion(csv_filename: str, source: str) -> None:
    if source not in ADAPTERS:
        raise ValueError(f"Unknown source: {source}. Supported: {list(ADAPTERS)}")

    csv_path = CSV_DATA_DIR / csv_filename
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    db = SessionLocal()
    try:
        raw_records = list(
            load_jobs_csv(
                path=csv_path, 
                source=source
            )
        )
        print(f"Loaded {len(raw_records)} raw records")

        adapter = ADAPTERS[source]
        canonical_jobs = [adapter(raw_record) for raw_record in raw_records]
        normalized_jobs = [normalize_job(canonical_job) for canonical_job in canonical_jobs]

        count = upsert_job_postings(db, normalized_jobs)
        print(f"Upserted {count} jobs")

    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

def ingest_csv_to_db(db: Session, csv_path: str | Path, source: str = "indeed_ca") -> int:
    path = Path(csv_path)

    adapter = ADAPTERS[source]
    raw_records = list(load_jobs_csv(path=path, source=source))
    canonical_jobs = (adapter(r) for r in raw_records)
    normalized_jobs = (normalize_job(j) for j in canonical_jobs)

    return upsert_job_postings(db, normalized_jobs)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, help="CSV filename inside app/ingestion/data/csv/")
    parser.add_argument("--source", default="indeed_ca", help="Source name tag")
    args = parser.parse_args()

    run_ingestion(
        csv_filename=args.csv, 
        source=args.source
    )

if __name__ == "__main__":
    main()
