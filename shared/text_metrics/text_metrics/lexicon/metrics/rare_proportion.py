from text_metrics.core.context import DocumentContext

METRIC_NAME = "rare_words_proportion"
METRIC_GROUP = "text"
    
def extract(context: DocumentContext):
    lexicon = context.lexicon
    if not lexicon:
        return 0
    
    rare_words = sum(count for count in lexicon.values() if count <= 2)
    total_words = lexicon.total()
    return rare_words / total_words