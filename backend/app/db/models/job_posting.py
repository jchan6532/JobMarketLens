import datetime
from sqlalchemy import String, Text, Date, UniqueConstraint, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class JobPosting(Base):
    __tablename__ = "job_postings"
    __table_args__ = (
        UniqueConstraint("source_name", "source_job_id", name="uq_job_source"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(255))

    company: Mapped[str] = mapped_column(String(255))

    description: Mapped[str] = mapped_column(Text)

    city: Mapped[str] = mapped_column(
        String(100), 
        index=True
    )

    province: Mapped[str] = mapped_column(
        String(100), 
        index=True
    )

    country: Mapped[str] = mapped_column(
        String(100), 
        default="Canada"
    )

    salary_min: Mapped[int | None] = mapped_column(
        Integer, 
        nullable=True
    )
    
    salary_max: Mapped[int | None] = mapped_column(
        Integer, 
        nullable=True
    )

    salary_raw: Mapped[str | None] = mapped_column(
        String(255), 
        nullable=True
    )

    posted_date: Mapped[datetime.date | None] = mapped_column(
        Date, 
        nullable=True, 
        index=True
    )
    
    role_category: Mapped[str | None] = mapped_column(String(50))

    source_name: Mapped[str] = mapped_column(
        String(100), 
        index=True, 
        nullable=False
    )

    source_job_id: Mapped[str] = mapped_column(
        String(500), 
        nullable=False
    )

    skills = relationship(
        "JobSkill",
        back_populates="job",
        cascade="all, delete-orphan",
    )
