from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True
    )

    slug: Mapped[str] = mapped_column(
        String(64), 
        unique=True, 
        index=True, 
        nullable=False
    )
    
    name: Mapped[str] = mapped_column(
        String(100), 
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(50),
        index=True,
        nullable=False,
    )

    job_skills = relationship(
        "JobSkill",
        back_populates="skill",
        cascade="all, delete-orphan",
    )
