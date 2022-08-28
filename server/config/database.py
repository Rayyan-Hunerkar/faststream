import motor.motor_asyncio
from beanie import init_beanie

from server.models import User
from .settings import mongosettings as settings


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        settings.uri
    )

    await init_beanie(database=client.faststream, document_models=[
        User
    ])
