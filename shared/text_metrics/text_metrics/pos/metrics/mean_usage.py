from collections import Counter
from text_metrics.core.context import DocumentContext
from text_metrics.pos.consts import set_of_pos

METRIC_GROUP = "pos"

def extract(context: DocumentContext):
    series = context.pos.get_series()
    sentences_count = context.pos.sentences_count
    
    pos_counter = Counter([span.data["pos"] for span in series ])
    used_in_set = pos_counter.keys() & set_of_pos

    return { f"mean_usage_{pos}" : pos_counter[pos] / sentences_count for pos in used_in_set }
