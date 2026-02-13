from text_metrics.core.span import Span
from text_metrics.external.natasha import money_extractor

TAG_NAME = "MEAS"

def tag(text):
    matches = money_extractor(text)
    return [ Span (match.start, match.stop, { "part": match.fact }) for match in matches ]
