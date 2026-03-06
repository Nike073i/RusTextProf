from predictors.serialization import load_model
from pathlib import Path
from cachetools import cached
from core.exceptions import app_error


@cached(cache={})
def load_predictor(file_name):
    file = Path(file_name)
    
    if not file.exists():
        raise app_error(message="Модель не найдена", errors=[f"Модель по пути {file_name} не найдена"])
    
    if file.suffix != '.pkl':
        raise app_error(message="Недопустимый формат модели", errors=[ f"Модель имеет недопустимый формат - {file.suffix}"])
    
    model = load_model(file)
    
    return model


async def get_profile(metrics, model_info):
    predictor = load_predictor(model_info.path)
    
    model_result = predictor.predict([metrics])
    
    return model_result[0]
