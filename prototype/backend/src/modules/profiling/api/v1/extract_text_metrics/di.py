from modules.profiling.use_cases.extract_text_metrics import ExtractTextMetricsUseCase
from modules.profiling.infrastructure.memory_cache.text import async_get_metrics

def resolve_extract_text_metrics_use_case():
    return ExtractTextMetricsUseCase(async_get_metrics)
