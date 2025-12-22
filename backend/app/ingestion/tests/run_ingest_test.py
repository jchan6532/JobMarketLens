from app.db.session import SessionLocal
from app.ingestion.loaders.csv_loader import load_jobs_csv
from app.ingestion.adapters.indeed_ca_adapter import adapt_indeed_ca
from app.ingestion.normalize import normalize_job
from app.ingestion.db_writer import upsert_job_postings

def main():
    raw_records = load_jobs_csv("app/ingestion/data/Job_list_Canada.csv", source_name="indeed_ca")
    canonical = (adapt_indeed_ca(r) for r in raw_records)
    normalized = (normalize_job(j) for j in canonical)

    db = SessionLocal()
    try:
        n = upsert_job_postings(db, normalized, commit_every=200)
        print(f"Upserted: {n}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
