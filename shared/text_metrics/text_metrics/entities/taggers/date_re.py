from text_metrics.entities.base.regex_tag import regex_tagger_factory

TAG_NAME = "DATE"

pattern = (
    r'\b((0?[1-9]|[12][0-9]|3[01])[./-](0?[1-9]|1[0-2])[./-](19|20)?\d{2}|'
    r'(19|20)\d{2}[./-](0?[1-9]|1[0-2])[./-](0?[1-9]|[12][0-9]|3[01])|'
    r'(0?[1-9]|1[0-2])[./-](0?[1-9]|[12][0-9]|3[01])[./-](19|20)?\d{2})\b'
)

tag = regex_tagger_factory(pattern)
