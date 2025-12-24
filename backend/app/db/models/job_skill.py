from sqlalchemy import ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class JobSkill(Base):
    __tablename__ = "job_skills"

    __table_args__ = (
        Index("ix_job_skills_job_id", "job_id"),
        Index("ix_job_skills_skill_id", "skill_id"),
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey(
            "job_postings.id", 
            ondelete="CASCADE"
        ),
        primary_key=True,
    )

    skill_id: Mapped[int] = mapped_column(
        ForeignKey(
            "skills.id",
            ondelete="CASCADE"
        ),
        primary_key=True,
    )

    job = relationship("JobPosting", back_populates="job_skills")
    skill = relationship("Skill", back_populates="job_skills")
