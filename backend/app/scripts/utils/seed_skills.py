from __future__ import annotations
from sqlalchemy.orm import Session

from app.db.models.skill import Skill
from app.nlp.skills_dictionary import SKILLS


def seed_skills(db: Session) -> dict[str, int]:
    """
    Insert skills if missing. Return {slug: skill_id}.
    """
    existing = {s.slug: s.id for s in db.query(Skill).all()}

    to_add: list[Skill] = []
    for slug, entry in SKILLS.items():
        if slug not in existing:
            to_add.append(Skill(slug=slug, name=entry.name, category=entry.category))

    if to_add:
        db.add_all(to_add)
        db.commit()

    # refresh mapping
    return {s.slug: s.id for s in db.query(Skill).all()}