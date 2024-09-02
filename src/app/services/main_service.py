import re

import pydash
from pymongo.results import InsertOneResult

from app.models import Content, SystemTag
from app.services.base import AppService, AppServiceParams


class MainService(AppService):
    def __init__(self, base_params: AppServiceParams) -> None:
        super().__init__(base_params)

    def create_content(self, title: str, link: str, content_tags_str: str, system_tags_str: str) -> InsertOneResult:
        content_tags = [tag for tag in re.split(r"[,\s]+", content_tags_str.lower()) if tag]
        content_tags = pydash.uniq(content_tags)

        system_tags = re.split(r"[,\s]+", system_tags_str.lower())
        system_tags = [SystemTag(tag) for tag in system_tags if tag]

        new_content = Content(
            title=title,
            link=link,
            content_tags=content_tags,
            system_tags=system_tags,
        )

        return self.db.content.insert_one(new_content)
