from text_metrics.core.context import DocumentContext

METRIC_NAME = "breadth_of_use_entities"
METRIC_GROUP = "entities"

def extract(context: DocumentContext):
    entities = context.entities
    breadth = len(entities.spans) / entities.entities_width
    return breadth