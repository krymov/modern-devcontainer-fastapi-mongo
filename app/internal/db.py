import motor.motor_asyncio
from beanie import init_beanie

from app.config import APP_SETTINGS


async def init_db() -> None:
    """Initailize the database connection."""
    client = motor.motor_asyncio.AsyncIOMotorClient(APP_SETTINGS.MONGO_DB)

    await init_beanie(
        database=client.starter,
        document_models=[],
    )
