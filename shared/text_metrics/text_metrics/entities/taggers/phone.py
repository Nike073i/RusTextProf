from phonenumbers import PhoneNumberMatcher
from text_metrics.core.span import Span

TAG_NAME = "PHONE"

def tag(text):
    matcher = PhoneNumberMatcher(text, region='ru')
    return [ Span(match.start, match.end, { "phone": match.raw_string }) for match in matcher ]
    