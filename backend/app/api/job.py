from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, nulls_last
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.job import JobResponse
from app.db.models.job_posting import JobPosting

router = APIRouter(
    prefix="/jobs", 
    tags=["jobs"]
)


@router.get("/", response_model=list[JobResponse])
def get_jobs(
    keyword: str | None = Query(None, description="Search title/description"),
    city: str | None = Query(None),
    province: str | None = Query(None),
    role_category: str | None = Query(None),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    order_by: str = Query("posted_date", description="posted_date|salary_min|salary_max|id"),
    order_dir: str = Query("desc", description="asc|desc"),
    db: Session = Depends(get_db)
) -> list[JobResponse]:
    keyword = keyword.strip() if keyword else None
    city = city.strip().lower() if city else None
    province = province.strip().upper() if province else None
    role_category = role_category.strip().lower() if role_category else None

    statement = select(JobPosting)

    if keyword:
        like = f"%{keyword}%"
        statement = statement.where(
            (JobPosting.title.ilike(like)) | 
            (JobPosting.description.ilike(like))
        )

    if city:
        statement = statement.where(JobPosting.city == city)
    
    if province:
        statement = statement.where(JobPosting.province == province)
    
    if role_category:
        statement = statement.where(JobPosting.role_category == role_category)
    
    col_map = {
        "posted_date": JobPosting.posted_date,
        "salary_min": JobPosting.salary_min,
        "salary_max": JobPosting.salary_max,
        "id": JobPosting.id
    }
    if order_by not in col_map:
        raise HTTPException(400, "order_by must be posted_date|salary_min|salary_max|id")
    
    sort_col = col_map.get(order_by, JobPosting.posted_date)

    dir = order_dir.lower()
    if dir not in ("asc", "desc"):
        raise HTTPException(
            status_code=400, 
            detail="order_dir must be 'asc' or 'desc'"
        )
    
    statement = statement.order_by(
        nulls_last(sort_col.asc() if dir == "asc" else sort_col.desc())
    )

    statement = statement.limit(limit).offset(offset)

    rows = db.execute(statement).scalars().all()

    return [JobResponse.model_validate(row) for row in rows]


@router.get("/{id}", response_model=JobResponse)
def get_job(
    id: int, 
    db: Session = Depends(get_db)
) -> JobResponse:
    job = db.get(JobPosting, id)

    if not job:
        raise HTTPException(
            status_code=404, 
            detail="Job not found"
        )
    
    return JobResponse.model_validate(job)