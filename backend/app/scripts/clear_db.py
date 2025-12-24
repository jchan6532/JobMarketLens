from sqlalchemy import text
from app.db.base import Base
from app.db.session import SessionLocal

def clear_database() -> None:
    db = SessionLocal()
    try:
        for table in Base.metadata.sorted_tables:
            db.execute(
                text(
                    f"TRUNCATE TABLE {table.name} RESTART IDENTITY CASCADE"
                )
            )
        db.commit()
        print("Database cleared.")
    finally:
        db.close()


if __name__ == "__main__":
    clear_database()
