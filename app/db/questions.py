import logging
from bson import ObjectId
from app.db.db import db

logger = logging.getLogger(__name__)

async def get_questions(quiz_id, limit=10):
    logger.info('call get questions with id %s', quiz_id)
    collection = db.questions
    documents = []
    async for document in collection.find({
        "quizId": ObjectId(quiz_id)
    }).limit(limit):
        documents.append(document)
    logger.info('get questions success')
    return documents