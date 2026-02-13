from collections import Counter
from text_metrics.core.context import DocumentContext

METRIC_NAME = "index_of_formality"
METRIC_GROUP = "pos"

def extract(context: DocumentContext):
    series = context.pos.get_series()
    
    pos_counter = Counter([span.data["pos"] for span in series ])
    
    def count_of(pos):
        return pos_counter[pos]
    
    formal = count_of("NOUN") + count_of("ADJ") + count_of("ADP")
    informal = (
        count_of("PRON") 
        + count_of("VERB") 
        + count_of("VERBPART")
        + count_of("VERBCONV")
        + count_of("PART")
        + count_of("ADV") 
        + count_of("CCONJ") + count_of("SCONJ")
        + count_of("INTJ")
    )
    
    fi = (formal - informal + 100) / 2
    return max(0, min(fi, 100))