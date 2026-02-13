from text_metrics.core.context import DocumentContext

METRIC_GROUP = "entities"

def extract(context: DocumentContext):
    entities = context.entities
    sentences_count = context.pos.sentences_count
    
    return { f"mean_usage_{entity}" : len(spans) / sentences_count for entity, spans in entities.spans.items() }
