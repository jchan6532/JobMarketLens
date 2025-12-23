from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.ingestion.runners.run_ingestion_csv import ingest_csv_to_db
from app.schemas.ingest import IngestCSVRequest, IngestResponse

router = APIRouter(
    prefix="/ingestion", 
    tags=["ingestion"]
)

@router.post("/csv", response_model=IngestResponse)
def ingest_csv(
    req: IngestCSVRequest, 
    db: Session = Depends(get_db)
) -> IngestResponse:
    count = ingest_csv_to_db(
        db=db, 
        csv_path=req.csv_path, 
        source=req.source
    )
    return IngestResponse(upserted=count)