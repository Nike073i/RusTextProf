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
    proportions = counts / counts.sum()
    
    return dict(zip(transitions, proportions.tolist()))
    