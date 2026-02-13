from text_metrics.core.context import DocumentContext

METRIC_NAME = "type_token_ratio"
METRIC_GROUP = "text"
    
def extract(context: DocumentContext):
    lexicon = context.lexicon
    if not lexicon:
        return 0

    unique_words = sum(count for count in lexicon.values() if count == 1)
    
    total_words = lexicon.total()
    return unique_words / total_words