from urlextract import URLExtract
from text_metrics.core.span import Span

extractor = URLExtract()

TAG_NAME = "URL"

def tag(text):
    return [ Span(start, end, { "link": url }) for (url, (start, end)) in extractor.find_urls(text, get_indices=True) ]
