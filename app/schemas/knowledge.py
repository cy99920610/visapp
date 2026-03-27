from datetime import date

from pydantic import BaseModel


class DocumentCreate(BaseModel):
    title: str
    category: str
    tags: str | None = None
    owner: str | None = None
    issue_date: date | None = None
    review_date: date | None = None
    content: str


class DocumentUpdate(BaseModel):
    title: str | None = None
    category: str | None = None
    tags: str | None = None
    owner: str | None = None
    issue_date: date | None = None
    review_date: date | None = None
    content: str | None = None
    changed_by: str = "system"
