from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from modules.profiling.use_cases.get_available_models import GetAvailableModelsUseCase
from .di import resolve_get_available_models_use_case

class Request(BaseModel):
    pass
    
class ProfilingModel(BaseModel):
    id: str
    name: str

class Response(BaseModel):
    available_models: List[ProfilingModel]

async def get_available_models(
    data: Request = Depends(),
    use_case: GetAvailableModelsUseCase = Depends(resolve_get_available_models_use_case)
):
    models = await use_case.execute()
    return {"available_models": models }

def register(router: APIRouter):
    router.get("/available-models", response_model=Response)(get_available_models)
