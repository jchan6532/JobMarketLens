from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
from app.db.models import job_posting
from app.db.models import skill
from app.db.models import job_skill
