import re
from app.ingestion.types.SalaryRange import SalaryRange

_RANGE_YEAR_RE = re.compile(
    r"""\$\s*([\d,]+)\s*-\s*\$\s*([\d,]+)\s*(?:a|per)\s*year""",
    re.IGNORECASE,
)

def parse_salary(salary: str | None) -> SalaryRange:
    if not salary:
        return SalaryRange(None, None, None)

    s = salary.strip()
    if not s:
        return SalaryRange(None, None, None)

    match = _RANGE_YEAR_RE.search(s)
    if match:
        lo = int(match.group(1).replace(",", ""))
        hi = int(match.group(2).replace(",", ""))
        if lo > hi:
            lo, hi = hi, lo
        return SalaryRange(lo, hi, "year")

    # fallback: unparsed format
    return SalaryRange(None, None, None)
