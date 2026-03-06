class GetAvailableModelsUseCase:
    def __init__(self, get_models_info):
        self._get_models_info = get_models_info
    
    async def execute(self):
        models_info = await self._get_models_info()
        
        return list(map(lambda model: { "id": model.id, "name": model.name }, models_info))