from __future__ import annotations

from app.nlp.role_rules import ROLE_RULES

def _norm(text: str | None) -> str:
    return (text or "").lower().strip()

def classify_role(title: str | None, description: str | None) -> str | None:
    haystack = f"{_norm(title)}\n{_norm(description)}"

    if not haystack.strip():
        return None

    for rule in ROLE_RULES:
        if rule.negative_keywords and any(neg in haystack for neg in rule.negative_keywords):
            continue
        if any(kw in haystack for kw in rule.keywords):
            return rule.role

    return None
