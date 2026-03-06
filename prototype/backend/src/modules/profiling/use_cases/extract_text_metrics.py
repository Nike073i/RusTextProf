class ExtractTextMetricsUseCase:
    def __init__(self, extract_metrics):
        self.extract_metrics = extract_metrics
        
    async def execute(self, text):
        metrics = await self.extract_metrics(text)
        return metrics