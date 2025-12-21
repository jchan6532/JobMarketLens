from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterator, Union

from app.ingestion.types.RawRecord import RawRecord

REQUIRED_COLUMNS = {
    "JobTitle",
    "Company",
    "Location",
    "PostDate",
    "Summary",
    "JobUrl",
    "Salary"
}


def load_jobs_csv(
    path: Union[str, Path],
    *,
    source: str,
    encoding: str = "utf-8",
) -> Iterator[RawRecord]:
    """
    Universal CSV loader for job datasets.
    - Reads rows as dicts (no normalization here)
    - Validates required columns exist
    - Yields RawRecord(source, payload, fetched_at)
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"CSV not found: {p}")

    fetched_at = (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
    )

    with p.open("r", encoding=encoding, newline="") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            raise ValueError("CSV has no header row (fieldnames missing).")

        missing = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing:
            raise ValueError(
                f"CSV missing required columns: {sorted(missing)}. "
                f"Found: {reader.fieldnames}"
            )

        for row in reader:
            payload = {k: (v if v is not None else "") for k, v in row.items()}
            yield RawRecord(source=source, payload=payload, fetched_at_utc=fetched_at)
