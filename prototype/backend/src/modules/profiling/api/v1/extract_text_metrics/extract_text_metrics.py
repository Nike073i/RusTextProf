from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from typing import Dict
from modules.profiling.use_cases.extract_text_metrics import ExtractTextMetricsUseCase
from .di import resolve_extract_text_metrics_use_case

class Request(BaseModel):
    text: str = Field(...,  max_length=10000, description="Текст")

class Response(BaseModel):
    metrics: Dict[str, Dict[str, float]]

async def extract_metrics(
    data: Request,
    use_case: ExtractTextMetricsUseCase = Depends(resolve_extract_text_metrics_use_case)
):
    metrics = await use_case.execute(data.text)
    return {"metrics": metrics }

def register(router: APIRouter):
    router.post("/text-metrics", response_model=Response)(extract_metrics)
