
from motor.motor_asyncio import AsyncIOMotorClient
from app.constants import MONGODB_URI
import datetime
import asyncio

mongo_client = AsyncIOMotorClient(MONGODB_URI)
db = mongo_client['quiz_db']

questions_collection = db["questions"]
quiz_collection = db["quiz"]

async def do_insert():
    quiz_doc = {
        "name": "New Quiz",
        "description": "new quiz data",
        "createdAt": datetime.datetime.now(tz=datetime.timezone.utc),
        "updatedAt": datetime.datetime.now(tz=datetime.timezone.utc),
    }

    result = await quiz_collection.insert_one(quiz_doc)
    print(f"Inserted single document with _id: {result.inserted_id}")

    question_docs = [
        {
            "quizId": result.inserted_id,
            "isActive": True,
            "content": "question test",
            "isMultipleChoice": False,
            "answers": [
                {
                    "id": 1,
                    "content": "1st answer",
                    "isCorrect": True
                },
                {
                    "id": 2,
                    "content": "2nd answer",
                    "isCorrect": False
                }
            ],
            "createdAt": datetime.datetime.now(tz=datetime.timezone.utc),
            "updatedAt": datetime.datetime.now(tz=datetime.timezone.utc),
        },
    ]
    result = await questions_collection.insert_many(question_docs)
    print(f"Inserted multiple documents with _ids: {result.inserted_ids}")
    
loop = mongo_client.get_io_loop()
loop.run_until_complete(do_insert())