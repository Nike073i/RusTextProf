from text_metrics.core.context import DocumentContext
from text_metrics.punct.consts import set_of_puncts

METRIC_NAME = "breadth_of_use_puncts"
METRIC_GROUP = "punct"

def extract(context: DocumentContext):
    series = context.pos.get_series()
    
    used_puncts_set = { span.data['text'] for span in series if span.data['pos'] == "PUNCT"}
    used_in_set = used_puncts_set.intersection(set_of_puncts)
    breadth = len(used_in_set) / len(set_of_puncts)
    return breadth

