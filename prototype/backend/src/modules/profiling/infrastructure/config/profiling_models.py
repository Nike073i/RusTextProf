from core.config import ProfilingSection
from core.exceptions import app_error, not_found_error


async def get_models_info(config):
    profiling = ProfilingSection.from_yaml(config)
    
    return profiling.models.values()


async def get_model_info(config, model_id=None):
    profiling = ProfilingSection.from_yaml(config)
    models = profiling.models
    
    if not models:
        raise app_error(message="Отсутствуют модели для прогнозирования")
    
    if model_id and model_id not in models:
        raise not_found_error(message="Указана несуществующая модель", errors=[f"Модель {model_id} не доступна для прогнозирования"])
    
    return models[model_id] if model_id else list(models.values())[0]
    