import datetime
from sqlalchemy import String, Text, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class JobPosting(Base):
    __tablename__ = "job_postings"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(255))

    company: Mapped[str] = mapped_column(String(255))

    description: Mapped[str] = mapped_column(Text)

    city: Mapped[str] = mapped_column(String(100))

    province: Mapped[str] = mapped_column(String(100))

    country: Mapped[str] = mapped_column(String(100), default="Canada")

    posted_date: Mapped[datetime.date | None] = mapped_column(Date, nullable=True)
    
    role_category: Mapped[str | None] = mapped_column(String(50))

    skills = relationship(
        "JobSkill",
        back_populates="job",
        cascade="all, delete-orphan",
    )
