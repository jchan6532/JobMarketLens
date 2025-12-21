from __future__ import annotations

import datetime
import re
from typing import Optional, Tuple

from app.ingestion.types.RawRecord import RawRecord
from app.ingestion.types.CanonicalJob import CanonicalJob


_LOC_RE = re.compile(r"^\s*(?P<city>.+?)\s*,\s*(?P<prov>[A-Za-z]{2})\s*$")


def split_location(location: str) -> Tuple[str, str]:
    """
    Expects formats like: 'Toronto, ON'
    Returns (city, province). Raises if bad format.
    """
    s = (location or "").strip()

    if s.lower() in {"remote", "canada remote", "remote (canada)", "canada, remote"}:
        return "Remote", "NA"
    
    m = _LOC_RE.match(location or "")
    if not m:
        raise ValueError(f"Unrecognized location format: {location!r}")
    return m.group("city").strip(), m.group("prov").upper().strip()


def parse_post_date(post_date: str) -> Optional[datetime.date]:
    """
    Dataset uses relative strings like:
      - '2 days ago'
      - '30+ days ago'
    For MVP: convert to an approximate date.
    """
    s = (post_date or "").strip().lower()
    if not s:
        return None

    today = datetime.date.today()

    if s == "30+ days ago":
        return today - datetime.timedelta(days=30)

    m = re.match(r"^(\d+)\s+day[s]?\s+ago$", s)
    if m:
        days = int(m.group(1))
        return today - datetime.timedelta(days=days)

    if s in {"today", "just posted"}:
        return today

    return None


def adapt_indeed_ca(raw: RawRecord) -> CanonicalJob:
    p = raw.payload

    title = (p.get("JobTitle") or "").strip()
    company = (p.get("Company") or "").strip()
    description = (p.get("Summary") or "").strip()
    location = (p.get("Location") or "").strip()
    job_url = (p.get("JobUrl") or "").strip()

    if not title or not company or not description or not location or not job_url:
        raise ValueError("Missing one of required fields: JobTitle/Company/Summary/Location/JobUrl")

    city, province = split_location(location)

    return CanonicalJob(
        title=title,
        company=company,
        description=description,
        city=city,
        province=province,
        country="Canada",
        posted_date=parse_post_date(p.get("PostDate", "")),
        source_name=raw.source,
        source_job_id=job_url,
    )
