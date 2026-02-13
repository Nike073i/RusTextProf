from text_metrics.core.context import DocumentContext

METRIC_NAME = "lexical_diversity_per_sentence"
METRIC_GROUP = "text"

def extract(context: DocumentContext):
    unique_words = sum(count for count in context.lexicon.values() if count == 1)
    return unique_words / context.pos.sentences_count