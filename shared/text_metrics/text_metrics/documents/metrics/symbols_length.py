from text_metrics.core.context import DocumentContext

METRIC_NAME = "symbols_length"
METRIC_GROUP = "text"

def extract(context: DocumentContext):
    return context.document_stat.symbols_length / context.pos.sentences_count