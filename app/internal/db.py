import motor.motor_asyncio
from beanie import Indexed, Link, PydanticObjectId, init_beanie

from ..config import APP_SETTINGS


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(APP_SETTINGS.MONGO_DB)

    await init_beanie(
        database=client.starter,
        document_models=[],
    )
