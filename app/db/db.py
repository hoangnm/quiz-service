
from motor.motor_asyncio import AsyncIOMotorClient
from app.constants import MONGODB_URI

mongo_client = AsyncIOMotorClient(MONGODB_URI)
db = mongo_client['quiz_db']