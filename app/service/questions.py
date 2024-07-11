import app.db.questions as questions_db

async def get_questions(quiz_id, limit):
    questions = await questions_db.get_questions(quiz_id, limit)
    return questions