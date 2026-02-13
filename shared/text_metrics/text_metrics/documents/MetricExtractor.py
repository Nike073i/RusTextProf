from ..core.context import DocumentContext
from ..core.metric import Metric
from collections import defaultdict

DEFAULT_GROUP = "common"

class MetricExtractor:
    def __init__(self, metrics: Metric):
        self._metrics = metrics
        
    def extract(self, context: DocumentContext):
        values = defaultdict(dict)

        for metric in self._metrics:
            value = metric.extract_func(context)
            group_name = metric.group or DEFAULT_GROUP
            group = values[group_name]
            
            if isinstance(value, dict):
                group.update(value)
            else:
                group[metric.name] = value
                
        return values
