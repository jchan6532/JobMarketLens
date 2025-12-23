from pydantic import BaseModel

class IngestCSVRequest(BaseModel):
    csv_path: str
    source: str


class IngestResponse(BaseModel):
    upserted: int