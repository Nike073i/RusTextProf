from text_metrics.core.context import DocumentContext
from text_metrics.core.span import Span
from nltk import ConditionalFreqDist, bigrams
import numpy as np

transitions = [
    ('ADJ-Pos', 'NOUN'),
    ('PROPN', 'PUNCT'),
    ('PUNCT', 'SCONJ'),
    ('ADP', 'ADJ-Pos'),
    ('ADP', 'PRON'),
    ('PUNCT', 'ADV'),
    ('PUNCT', 'PRON'),
    ('ADJ-Pos', 'PUNCT'),
    ('PUNCT', 'CCONJ')
]

METRIC_GROUP = "pos"
    
def extract(context: DocumentContext):
    series = context.pos.get_series(
        seq_start=Span(-1, -1, { "code": "START" }), 
        seq_end=Span(-1, -1, { "code": "END" })
    )
    
    cfd = ConditionalFreqDist()
    for (tag1, tag2) in bigrams([ span.data['code'] for span in series ]):
        cfd[tag1][tag2] += 1
        
    counts = np.array([ cfd[condition][tag] for condition, tag in transitions ])
    all_sum = counts.sum()
    if all_sum != 0:
        proportions = counts / counts.sum()
    else:
        proportions = np.zeros_like(counts)

    return dict(zip(transitions, proportions.tolist()))
    