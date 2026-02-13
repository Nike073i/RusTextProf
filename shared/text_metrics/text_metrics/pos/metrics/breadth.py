from text_metrics.core.context import DocumentContext
from text_metrics.pos.consts import set_of_pos

METRIC_NAME = "breadth_of_use_pos"
METRIC_GROUP = "pos"

def extract(context: DocumentContext):
    series = context.pos.get_series()
    
    used_pos = { span.data["pos"] for span in series }    
    used_in_set = used_pos.intersection(set_of_pos)
    breadth = len(used_in_set) / len(set_of_pos)
    return breadth
        