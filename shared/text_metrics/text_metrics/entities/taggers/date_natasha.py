from text_metrics.core.span import Span
from text_metrics.external.natasha import dates_extractor

TAG_NAME = "DATE"

def tag(text):
    matches = dates_extractor(text)
    return [ Span (match.start, match.stop, { "part": match.fact }) for match in matches ]
