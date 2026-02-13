import re
from ...core.span import Span

def regex_tagger_factory(pattern):
    regex = re.compile(pattern, re.IGNORECASE)   
    
    def tag(text):
        matches = regex.finditer(text)
        
        return [ Span(match.start(), match.end(), { "match": match.group(0) }) for match in matches ]
        
    return tag
