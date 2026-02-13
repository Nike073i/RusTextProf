from text_metrics.entities.base.regex_tag import regex_tagger_factory

TAG_NAME = "MEAS"

tag = regex_tagger_factory(r'(\d+[\d.,]*)\s*(кг|кило|шт|штук|ед|г|м|см|км|л|сек|мин|ч|лет|год)\b')
