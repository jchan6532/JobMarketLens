from app.ingestion.loaders.csv_loader import load_jobs_csv
from app.ingestion.adapters.indeed_ca_adapter import adapt_indeed_ca

CSV_PATH = "app/ingestion/data/Job_list_Canada.csv/Job_list_Canada.csv"

count = 0
for raw in load_jobs_csv(CSV_PATH, source="indeed_ca"):
    job = adapt_indeed_ca(raw)
    print(job.title, "->", job.city, job.province)
    count += 1
    if count >= 5:
        break

print("Loaded:", count)
