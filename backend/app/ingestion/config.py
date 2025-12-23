from pathlib import Path
from app.ingestion.adapters.indeed_ca_adapter import adapt_indeed_ca

CSV_DATA_DIR = Path(__file__).parent / "data" / "csv"
JSON_DATA_DIR = Path(__file__).parent / "data" / "json"

ADAPTERS = {
    "indeed_ca": adapt_indeed_ca,
}