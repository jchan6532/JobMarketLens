from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
from app.db.models import job_posting  # noqa: E402, F401
from app.db.models import skill        # noqa: E402, F401
from app.db.models import job_skill    # noqa: E402, F401
