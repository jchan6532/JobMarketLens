from __future__ import annotations
from dataclasses import dataclass

ROLE_LABELS = (
    "frontend",
    "backend",
    "fullstack",
    "data",
    "mobile",
    "devops",
)

@dataclass(frozen=True)
class RoleRule:
    role: str
    keywords: tuple[str, ...]
    # if any of these appear, we block the rule
    negative_keywords: tuple[str, ...] = ()

ROLE_RULES: tuple[RoleRule, ...] = (
    RoleRule(
        role="fullstack",
        keywords=("full stack", "full-stack", "fullstack"),
    ),
    RoleRule(
        role="frontend",
        keywords=("frontend", "front end", "front-end", "ui", "web developer"),
        negative_keywords=("backend", "back end", "back-end"),
    ),
    RoleRule(
        role="backend",
        keywords=("backend", "back end", "back-end", "api", "server-side"),
        negative_keywords=("frontend", "front end", "front-end"),
    ),
    RoleRule(
        role="mobile",
        keywords=("mobile", "ios", "android", "react native", "react-native"),
    ),
    RoleRule(
        role="data",
        keywords=("data engineer", "data scientist", "machine learning", "ml", "ai", "analytics"),
    ),
    RoleRule(
        role="devops",
        keywords=("devops", "site reliability", "sre", "platform engineer", "cloud engineer"),
    ),
)
