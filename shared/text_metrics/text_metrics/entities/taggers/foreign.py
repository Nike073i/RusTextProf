from text_metrics.entities.base.regex_tag import regex_tagger_factory

TAG_NAME = "FOREIGN"

tag = regex_tagger_factory(r'\b[a-z]+(-[a-zA-Z]+)*\b')
