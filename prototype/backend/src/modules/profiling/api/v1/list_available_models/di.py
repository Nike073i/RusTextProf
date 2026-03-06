from fastapi import Depends
from modules.profiling.use_cases.get_available_models import GetAvailableModelsUseCase
from modules.profiling.infrastructure.config.profiling_models import get_models_info
from core.config import resolve_config
from functools import partial

def resolve_get_available_models_use_case(config = Depends(resolve_config)):
    get_models_info_from_config = partial(get_models_info, config)
    return GetAvailableModelsUseCase(get_models_info_from_config)
