from text_metrics.core.span import Span
from text_metrics.external.natasha import addr_extractor

TAG_NAME = "ADDRESS"

def tag(text):
    matches = addr_extractor(text)
    return [ Span (match.start, match.stop, { "part": match.fact }) for match in matches ]
