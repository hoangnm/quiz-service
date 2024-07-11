from fastapi import APIRouter, HTTPException
from pydantic import ConfigDict, BaseModel, Field
import app.service.questions as questions_svc
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
from typing import Optional, List

router = APIRouter()

PyObjectId = Annotated[str, BeforeValidator(str)]

class QuestionResponseModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    content: str = Field(...)
    quizId: PyObjectId = Field(...)
    isMultipleChoice: bool = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        extra='ignore'
    )

class QuestionResponsesCollection(BaseModel):
    questions: List[QuestionResponseModel]

@router.get("/{quiz_id}", response_model=QuestionResponsesCollection)
async def get_questions(quiz_id: str, limit: int = 10):
    if not quiz_id:
        return HTTPException(status_code=400, detail="quiz_id is required")
    questions = await questions_svc.get_questions(quiz_id, limit)
    return QuestionResponsesCollection(questions=questions)