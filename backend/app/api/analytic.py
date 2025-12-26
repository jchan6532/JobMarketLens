from __future__ import annotations
from typing import Literal
from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, desc, cast, Date
from sqlalchemy.orm import Session
from datetime import date

from app.db.session import get_db
from app.db.models.job_posting import JobPosting
from app.db.models.skill import Skill
from app.db.models.job_skill import JobSkill
from app.schemas.analytic import (
    RoleCount, 
    CityCount,
    SkillCount,
    SkillTrendPoint
)


router = APIRouter(
    prefix="/analytics", 
    tags=["analytics"]
)

@router.get("/top-skills", response_model=list[SkillCount])
def get_top_skills(
    limit: int = Query(10, ge=1, le=100),
    city: str | None = None,
    role_category: str | None = None,
    date_from: date | None = None,
    date_to: date | None = None,
    db: Session = Depends(get_db)
) -> list[SkillCount]:
    query = (
        db.query(
            Skill.slug.label("slug"),
            Skill.name.label("name"),
            Skill.category.label("category"),
            func.count(func.distinct(JobSkill.job_id)).label("job_count"),
        )
        .select_from(JobSkill)
        .join(Skill, Skill.id == JobSkill.skill_id)
        .join(JobPosting, JobPosting.id == JobSkill.job_id)
    )

    if city:
        query = query.filter(JobPosting.city == city)
    if role_category:
        query = query.filter(JobPosting.role_category == role_category)
    if date_from:
        query = query.filter(JobPosting.posted_date >= date_from)
    if date_to:
        query = query.filter(JobPosting.posted_date <= date_to)

    rows = (
        query
        .group_by(Skill.slug, Skill.name, Skill.category)
        .order_by(desc("job_count"))
        .limit(limit)
        .all()
    )

    return [
        SkillCount(
            slug=row.slug, 
            name=row.name, 
            category=row.category, 
            count=int(row.job_count)
        ) for row in rows
    ]

@router.get("/skill-trend", response_model=list[SkillTrendPoint])
def get_skill_trend(
    skill: str = Query(
        ..., 
        alias="skill_slug", 
        min_length=1, 
        description="Skill slug (e.g. python, react, docker)"
    ),
    city: str | None = None,
    role_category: str | None = None,
    granularity: Literal["month", "week"] = Query(
        "month",
        description="Granularity of the trend data"
    ),
    date_from: date | None = None,
    date_to: date | None = None,
    db: Session = Depends(get_db)
) -> list[SkillTrendPoint]:

    period_start = cast(
        func.date_trunc(
            granularity, 
            JobPosting.posted_date
        ),
        Date,
    ).label("period_start")

    query = (
        db.query(
            period_start,
            func.count(func.distinct(JobPosting.id)).label("job_count"),
        )
        .select_from(JobSkill)
        .join(Skill, Skill.id == JobSkill.skill_id)
        .join(JobPosting, JobPosting.id == JobSkill.job_id)
        .filter(JobPosting.posted_date.isnot(None))
        .filter(
            (Skill.slug == skill) | (Skill.name.ilike(skill))
        )
    )

    if city:
        query = query.filter(JobPosting.city == city)
    if role_category:
        query = query.filter(JobPosting.role_category == role_category)
    if date_from:
        query = query.filter(JobPosting.posted_date >= date_from)
    if date_to:
        query = query.filter(JobPosting.posted_date <= date_to)

    rows = (
        query
        .group_by(period_start)
        .order_by(period_start.asc())
        .all()
    )

    return [
        SkillTrendPoint(
            period_start=row.period_start, 
            count=int(row.job_count)
        ) for row in rows
    ]

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

    return [
        CityCount(
            city=row.city, 
            count=int(row.job_count)
        ) for row in rows
    ]

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

    return [
        RoleCount(
            role_category=row.role_category, 
            count=int(row.job_count)
        ) for row in rows
    ]