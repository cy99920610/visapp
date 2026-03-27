from pydantic import BaseModel


class CommunicationCreate(BaseModel):
    channel: str
    direction: str = "inbound"
    summary: str
    payload: str | None = None
    contact_id: int | None = None
    company_id: int | None = None
