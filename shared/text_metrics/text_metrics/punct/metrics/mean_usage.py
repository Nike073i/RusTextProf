from collections import Counter
from text_metrics.core.context import DocumentContext
from text_metrics.punct.consts import set_of_puncts

METRIC_GROUP = "punct"

def extract(context: DocumentContext):
    sentences_count = context.pos.sentences_count
    series = context.pos.get_series()
    
    punct_counter = Counter([ span.data['text'] for span in series if span.data['pos'] == "PUNCT" ])
    
    used_in_set = punct_counter.keys() & set_of_puncts

    return { f"mean_usage_{punct}" : punct_counter[punct] / sentences_count for punct in used_in_set }
