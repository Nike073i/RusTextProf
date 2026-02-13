from text_metrics.core.context import DocumentContext

LONG_SENTENCE_LENGTH = 8

METRIC_NAME = "long_sentences_proportion"
METRIC_GROUP = "text"

def extract(context: DocumentContext):
    sentences_count = context.pos.sentences_count
    if sentences_count == 0: return 0

    long_count = sum(1 for seq in context.pos.seqs if len(seq) >= LONG_SENTENCE_LENGTH)

    return long_count  / sentences_count