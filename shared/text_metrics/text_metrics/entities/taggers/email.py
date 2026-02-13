from text_metrics.entities.base.regex_tag import regex_tagger_factory

TAG_NAME = "EMAIL"

tag = regex_tagger_factory(r'\b[\w\.-]+@[\w\.-]+\.\w+\b')
