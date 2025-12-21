from dataclasses import dataclass

@dataclass(frozen=True)
class SalaryRange:
    salary_min: int | None
    salary_max: int | None
    period: str | None