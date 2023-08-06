from __future__ import annotations

from typing import Awaitable

from caronte_common.data.db_document import Document
from caronte_common.interfaces.command import AsyncCommand
from pymongo.collection import Collection


class MongoConfigDocument(AsyncCommand[None]):
    def __init__(self, database: Collection, document: Document[Collection]) -> None:
        self.document = document
        self.document.instance = database.get_collection(
            self.document.name, **self.document.config
        )

    async def execute(self) -> Awaitable[None]:
        _map = {
            "create_index": lambda field_name, params: self.document.instance.create_index(
                field_name, **params
            )
        }
        for field_config in self.document.field_config:
            await _map[field_config.config_type](
                field_name=field_config.field_name,
                params=field_config.params,
            )
