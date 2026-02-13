from text_metrics.entities.base.regex_tag import regex_tagger_factory

TAG_NAME = "ENUM"

tag = regex_tagger_factory(r'(?<!\S)(\d+|[a-zA-Z]+)[.)](?!\d|\w)(?=\s|$)')
