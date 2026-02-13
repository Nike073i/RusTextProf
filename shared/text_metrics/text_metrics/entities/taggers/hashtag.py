from text_metrics.entities.base.regex_tag import regex_tagger_factory

TAG_NAME = "TAG"

tag = regex_tagger_factory(r'(?<!\w)#[a-zA-Zа-яА-ЯёЁ\d_]+(?=\W|$)')
