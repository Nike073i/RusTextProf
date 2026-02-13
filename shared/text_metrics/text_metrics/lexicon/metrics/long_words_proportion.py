from text_metrics.core.context import DocumentContext

LONG_WORD_LENGTH = 6

METRIC_NAME = "long_words_proportion"
METRIC_GROUP = "text"

def extract(context: DocumentContext):
    lexicon = context.lexicon
    if not lexicon:
        return 0
    
    long_words = sum(count for word, count in lexicon.items() if len(word) >= LONG_WORD_LENGTH)
    total_words = lexicon.total()
    return long_words / total_words