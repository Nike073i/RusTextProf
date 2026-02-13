from text_metrics.core.context import DocumentContext

METRIC_NAME = "lexicon_size"
METRIC_GROUP = "text"

def extract(context: DocumentContext):
    return len(context.lexicon) / context.pos.sentences_count