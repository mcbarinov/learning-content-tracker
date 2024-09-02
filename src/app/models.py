from __future__ import annotations

from datetime import datetime
from enum import Enum, unique

from mm_mongo import MongoModel, ObjectIdStr
from mm_std import utc_now
from pydantic import Field


@unique
class SystemTag(str, Enum):
    VIDEO = "video"
    BOOK = "book"
    IN_PROCESS = "in_process"
    LIKE = "like"
    SKIP = "skip"


class Content(MongoModel):
    id: ObjectIdStr | None = Field(None, alias="_id")
    title: str
    link: str
    created_at: datetime = Field(default_factory=utc_now)
    finished_at: datetime | None = None
    content_tags: list[str]
    system_tags: list[SystemTag]
    notes: str = ""

    __collection__ = "content"
    __indexes__ = "!link, content_tags, system_tags, created_at, finished_at"
