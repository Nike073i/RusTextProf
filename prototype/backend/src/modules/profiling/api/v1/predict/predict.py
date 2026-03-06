from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field, field_validator
from typing import Dict, Optional
from core.schemas import ErrorResponse
from modules.profiling.use_cases.predict_profile import PredictProfileUseCase
from .di import resolve_predict_profile_use_case


class Request(BaseModel):
    text: str = Field(..., min_length=300, max_length=10000, description="Текст")
    model_id: Optional[str] = Field(None, description="Идентификатор модели прогнозирования")
    
    @field_validator("text")
    def validate_quotes(value: str) -> str:
        double_quotes = value.count('"')
        single_quotes = value.count("'")
        if single_quotes % 2 != 0 or double_quotes % 2 != 0:
            raise ValueError('Количество кавычек должно быть четным')
        return value

class Prediction(BaseModel):
    proba: float
    threshold: float
    label: str

class Response(BaseModel):
    gender_prediction: Prediction
    age_prediction: Prediction
    metrics: Dict[str, Dict[str, float]]
    model_id: str

async def predict(
    data: Request,
    use_case: PredictProfileUseCase = Depends(resolve_predict_profile_use_case)
):
    result = await use_case.execute(data.text, data.model_id)
    
    return {
        "metrics": result.metrics,
        "gender_prediction": result.gender, 
        "age_prediction": result.age, 
        "model_id": result.model_id
    }

def register(router: APIRouter):
    router.post(
        "/predict", 
        response_model=Response,
        responses={
            404: {"model": ErrorResponse, "description": "Модель не найдена"},
            412: {"model": ErrorResponse, "description": "Извлеченные метрики невалидны для прогнозирования"},
            500: {"model": ErrorResponse, "description": "Внутренняя ошибка приложения"}
        }
    )(predict)
