from mm_base1.db import BaseDB, DatabaseAny
from mm_mongo import MongoCollection

from app.models import Content


class DB(BaseDB):
    def __init__(self, database: DatabaseAny):
        super().__init__(database)
        self.content: MongoCollection[Content] = Content.init_collection(database)
