from text_metrics.core.context import DocumentContext
import math

METRIC_NAME = "normalized_shannon_entropy"
METRIC_GROUP = "text"

def extract(context: DocumentContext):
    lexicon = context.lexicon
    if not lexicon:
        return 0.0

    max_freq = lexicon.most_common(1)[0][1]

    if max_freq == 1:
        return 1.0

    total_words = lexicon.total()

    entropy = 0.0
    for count in lexicon.values():
        p = count / total_words
        if p > 0:
            entropy -= p * math.log2(p)

    return entropy / math.log2(max_freq)