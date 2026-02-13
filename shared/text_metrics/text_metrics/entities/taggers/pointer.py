from text_metrics.entities.base.regex_tag import regex_tagger_factory

TAG_NAME = "POINTER"

tag = regex_tagger_factory(r'(пункт|п\.|раздел|гл|глава|статья|ст\.|№)\s+\d+[\d.-]*')
