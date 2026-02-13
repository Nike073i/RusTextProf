from collections import Counter
from text_metrics.core.context import DocumentContext

METRIC_NAME = "index_of_formality_tuldava"
METRIC_GROUP = "pos"

def extract(context: DocumentContext):
    series = context.pos.get_series()
    pos_counter = Counter([span.data["pos"] for span in series])
    
    def count_of(pos):
        return pos_counter[pos]
    
    formal = count_of("NOUN") + count_of("ADJ")
    informal = count_of("VERB") + count_of("ADV") + count_of("PRON")
    
    if informal == 0:
        return 100 if formal > 0 else 50
    
    fi = (formal / informal) * 100
    return min(fi, 100)