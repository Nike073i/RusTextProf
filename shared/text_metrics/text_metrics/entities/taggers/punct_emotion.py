from text_metrics.entities.base.regex_tag import regex_tagger_factory

TAG_NAME = "PUNCEM"

tag = regex_tagger_factory(r'[.!?]{2,}')
