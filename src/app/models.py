from datetime import datetime

from mm_mongo import MongoModel, ObjectIdStr
from pydantic import Field


class Content(MongoModel):
    id: ObjectIdStr | None = Field(None, alias="_id")
    name: str
    author: str
    link: str
    date: datetime
    content_tags: list[str]
    system_tags: list[str]

    __collection__ = "content"
    __indexes__ = "!link, date, content_tags, system_tags"
