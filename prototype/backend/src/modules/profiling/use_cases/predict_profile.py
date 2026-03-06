from ..domain.text import validate_metrics
from core.exceptions import validation_error


class PredictionResult:
    def __init__(self, gender, age, metrics, model_id):
        self.gender = gender
        self.age = age
        self.metrics = metrics
        self.model_id = model_id


class PredictProfileUseCase:
    def __init__(self, extract_metrics, get_profile, get_model_info):
        self.extract_metrics = extract_metrics
        self.get_profile = get_profile
        self.get_model_info = get_model_info
        
    async def execute(self, text, model_id=None):
        model_info = await self.get_model_info(model_id)
        
        metrics = await self.extract_metrics(text)
        
        errors = validate_metrics(metrics)
        
        if errors:
            raise validation_error(message="Извлеченные метрики невалидны для прогнозирования", errors=errors)
        
        profile = await self.get_profile(metrics, model_info)
        
        return PredictionResult(
            metrics=metrics, 
            gender=profile[0], 
            age=profile[1],
            model_id=model_info.id
        )
