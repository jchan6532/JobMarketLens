from app.ingestion.loaders.csv_loader import load_jobs_csv
from app.ingestion.adapters.indeed_ca_adapter import adapt_indeed_ca
from app.ingestion.normalize import normalize_job
from app.ingestion.db_writer import upsert_job_postings
from app.db.session import SessionLocal


def run_ingestion(csv_path: str) -> None:
    db = SessionLocal()
    try:
        raw_records = list(
            load_jobs_csv(
                path=csv_path, 
                source="indeed_ca"
            )
        )
        print(f"Loaded {len(raw_records)} raw records")

        canonical_jobs = [adapt_indeed_ca(raw_record) for raw_record in raw_records]
        normalized_jobs = [normalize_job(canonical_job) for canonical_job in canonical_jobs]

        count = upsert_job_postings(db, normalized_jobs)
        print(f"Upserted {count} jobs")

    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    run_ingestion("app/ingestion/data/Job_list_Canada.csv/Job_list_Canada.csv")
