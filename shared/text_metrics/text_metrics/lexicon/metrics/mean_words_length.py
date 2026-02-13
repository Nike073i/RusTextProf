from text_metrics.core.context import DocumentContext

METRIC_NAME = "mean_words_length"
METRIC_GROUP = "text"

def extract(context: DocumentContext):
    lexicon = context.lexicon
    if not lexicon:
        return 0
    
    total_chars = sum(len(word) * count for word, count in lexicon.items())
    total_words = lexicon.total()
    return total_chars / total_words