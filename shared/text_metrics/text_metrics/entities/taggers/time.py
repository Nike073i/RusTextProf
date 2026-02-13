from text_metrics.entities.base.regex_tag import regex_tagger_factory

TAG_NAME = "TIME"

tag = regex_tagger_factory(r'\b(0?[0-9]|1[0-9]|2[0-3])[:ч.,\s-][0-5][0-9]\b')
