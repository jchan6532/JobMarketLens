from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.base import Base
from app.core.config import get_settings
from app.db.session import get_db
from app.schemas.admin import AdminResetRequest

router = APIRouter(
    prefix="/admin", 
    tags=["admin"]
)

@router.post("/reset-db")
def reset_db_endpoint(
    data: AdminResetRequest,
    db: Session = Depends(get_db),
):
    settings = get_settings()
    ADMIN_PASSWORD = settings.ADMIN_PASSWORD
    ENV = settings.ENV

    if ENV.lower() not in {"dev", "development"}:
        raise HTTPException(
            status_code=403, 
            detail="Not allowed"
        )

    if data.admin_password != ADMIN_PASSWORD:
        raise HTTPException(
            status_code=401, 
            detail="Invalid admin password"
        )

    for table in Base.metadata.sorted_tables:
        db.execute(text(f"TRUNCATE TABLE {table.name} RESTART IDENTITY CASCADE"))
    db.commit()
    return {"detail": "Database cleared"}
