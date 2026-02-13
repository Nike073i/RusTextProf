from text_metrics.core.context import DocumentContext

METRIC_NAME = "pair_of_adv_per_sentence"
METRIC_GROUP = "pos"

def extract(context: DocumentContext):
    sentences_count = context.pos.sentences_count
    
    if sentences_count < 1:
        return 0
        
    count = 0
    for seq in context.pos.seqs:
        for i in range(1, len(seq)):
            prev = seq[i - 1]
            curr = seq[i]
            if prev.data['pos'] == "ADV" and curr.data['pos'] == "ADV":
                count += 1
                i += 2 
            else:
                i += 1
        
    return count / sentences_count    