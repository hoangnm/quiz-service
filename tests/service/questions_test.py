from unittest.mock import AsyncMock
from app.service.questions import get_questions
import pytest

@pytest.fixture()
def mock_get_questions_db(mocker):
    async_mock = AsyncMock()
    mocker.patch('app.db.questions.get_questions', side_effect=async_mock)
    return async_mock

@pytest.mark.asyncio
async def test_get_questions_service(mock_get_questions_db):
    mock_get_questions_db.return_value = [{'question': 'What is your name?'}]
    questions = await get_questions(quiz_id=1, limit=1)
    assert questions == [{'question': 'What is your name?'}]
