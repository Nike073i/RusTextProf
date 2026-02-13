from text_metrics.entities.base.regex_tag import regex_tagger_factory

TAG_NAME = "NUMBER"

tag = regex_tagger_factory(r'\b[\+-]?\d+([.,]\d+)?\b')
