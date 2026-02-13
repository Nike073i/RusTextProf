from text_metrics.core.context import DocumentContext

METRIC_NAME = "sentences_count"
METRIC_GROUP = "text"

def extract(context: DocumentContext):
    return context.pos.sentences_count