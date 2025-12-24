from __future__ import annotations

from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, desc
from sqlalchemy.orm import Session
from datetime import date

from app.db.session import get_db
from app.db.models.job_posting import JobPosting
from app.schemas.analytic import (
    RoleCount, 
    CityCount
)


router = APIRouter(
    prefix="/analytics", 
    tags=["analytics"]
)


@router.get("/top-cities", response_model=list[CityCount])
def get_top_cities(
    limit: int = Query(10, ge=1, le=100),
    role_category: str | None = None,
    date_from: date | None = None,
    date_to: date | None = None,
    db: Session = Depends(get_db)
) -> list[CityCount]:
    query = db.query(
        JobPosting.city.label("city"),
        func.count(JobPosting.id).label("job_count"),
    )

    if role_category:
        query = query.filter(JobPosting.role_category == role_category)
    if date_from:
        query = query.filter(JobPosting.posted_date >= date_from)
    if date_to:
        query = query.filter(JobPosting.posted_date <= date_to)

    rows = (
        query.filter(JobPosting.city.isnot(None))
        .group_by(JobPosting.city)
        .order_by(desc("job_count"))
        .limit(limit)
        .all()
    )

    return [CityCount(city=row.city, count=int(row.job_count)) for row in rows]

@router.get("/top-roles", response_model=list[RoleCount])
def get_top_roles(
    limit: int = Query(10, ge=1, le=100),
    city: str | None = None,
    date_from: date | None = None,
    date_to: date | None = None,
    db: Session = Depends(get_db)
) -> list[RoleCount]:
    query = db.query(
        JobPosting.role_category.label("role_category"),
        func.count(JobPosting.id).label("job_count"),
    )

    if city:
        query = query.filter(JobPosting.city == city)
    if date_from:
        query = query.filter(JobPosting.posted_date >= date_from)
    if date_to:
        query = query.filter(JobPosting.posted_date <= date_to)

    rows = (
        query.filter(JobPosting.role_category.isnot(None))
        .group_by(JobPosting.role_category)
        .order_by(desc("job_count"))
        .limit(limit)
        .all()
    )

    return [RoleCount(role_category=row.role_category, count=int(row.job_count)) for row in rows]