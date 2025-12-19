from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from app.db.models import job_posting, skill, job_skill