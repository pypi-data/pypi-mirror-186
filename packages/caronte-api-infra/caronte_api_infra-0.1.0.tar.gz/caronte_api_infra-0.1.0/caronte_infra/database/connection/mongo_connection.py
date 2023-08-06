from __future__ import annotations

from typing import Awaitable

from caronte_common.interfaces.command import AsyncCommand
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection


class MongoConnection(AsyncCommand[Collection]):
    def __init__(
        self,
        user: str,
        pwd: str,
        host: str,
        port: int,
        db_name: str,
    ) -> None:
        self.user = user
        self.pwd = pwd
        self.host = host
        self.port = port
        self.db_name = db_name

    async def execute(self) -> Awaitable[Collection]:
        client = AsyncIOMotorClient(
            f"mongodb://{self.user}:{self.pwd}@{self.host}:{self.port}"
        )
        database = client[self.db_name]
        return database


# async def main():
#     from bson.binary import UuidRepresentation
#     from bson.codec_options import CodecOptions

#     document = Document[Collection](
#         field_config=[
#             FieldConfig(
#                 field_name="Adm.Email",
#                 params={"unique": True},
#                 config_type="create_index",
#             ),
#             FieldConfig(
#                 field_name="Adm.Cellphone",
#                 params={"unique": True},
#                 config_type="create_index",
#             ),
#             FieldConfig(
#                 field_name="Adm.ExternalId",
#                 params={"unique": True},
#                 config_type="create_index",
#             ),
#             FieldConfig(
#                 field_name="Adm.UserName",
#                 params={"unique": True},
#                 config_type="create_index",
#             ),
#         ],
#         config={
#             "codec_options": CodecOptions(
#                 uuid_representation=UuidRepresentation.STANDARD
#             )
#         },
#         name="project",
#     )

#     connection = MongoConnection(
#         user="root",
#         pwd="MongoDB2019!",
#         host="localhost",
#         port=27017,
#         db_name="CaronteAuthDB",
#     )
#     database = await connection.execute()
#     config = MongoConfigDocument(database=database, document=document)
#     await config.execute()
#     print(document)
#     await document.instance.insert_one({"name": "asdasd"})


# if __name__ == "__main__":
#     asyncio.run(main())
