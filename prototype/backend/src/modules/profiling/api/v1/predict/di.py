from fastapi import Depends
from modules.profiling.use_cases.predict_profile import PredictProfileUseCase
from modules.profiling.infrastructure.config.profiling_models import get_model_info
from modules.profiling.infrastructure.memory_cache.text import async_get_metrics
from modules.profiling.infrastructure.ai_models.profiling import get_profile
from core.config import resolve_config
from functools import partial


def resolve_predict_profile_use_case(config = Depends(resolve_config)):
    get_model_info_from_config = partial(get_model_info, config)
    get_profile_by_local_predictor = get_profile
    
    return PredictProfileUseCase(async_get_metrics, get_profile_by_local_predictor, get_model_info_from_config)
