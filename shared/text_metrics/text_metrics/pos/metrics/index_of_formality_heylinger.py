from collections import Counter
from text_metrics.core.context import DocumentContext

METRIC_NAME = "index_of_formality_heylinger"
METRIC_GROUP = "pos"

def extract(context: DocumentContext):
    series = context.pos.get_series()
    
    pos_counter = Counter([span.data["pos"] for span in series ])
    
    def count_of(pos):
        return pos_counter[pos]
    
    formal = count_of("NOUN") + count_of("ADJ") + count_of("ADP") + count_of("DET") 
    informal = count_of("PRON") + count_of("VERB") + count_of("ADV") + count_of("INTJ") + count_of("NUM")

    total = formal + informal
    if total == 0:
        return 50
    
    return (formal / total) * 100
