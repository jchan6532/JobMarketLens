from __future__ import annotations

from app.nlp.skills_dictionary import SKILLS


def extract_skills(text: str) -> set[str]:
    if not text:
        return set()

    text_lower = text.lower()
    found: set[str] = set()

    for slug, skill in SKILLS.items():
        for alias in skill.aliases:
            if alias in text_lower:
                found.add(slug)
                break

    return found