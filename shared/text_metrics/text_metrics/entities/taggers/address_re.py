from text_metrics.entities.base.regex_tag import regex_tagger_factory

TAG_NAME = "ADDRESS"

pattern = (
    r'\b(ул\.|улица|просп\.|проспект|б[- ]?р\.|бульвар|пл\.|площадь|'
    r'пер\.|переулок|проезд)\s*([а-яА-Я-]+(\s*[а-яА-Я-]+)*)'
    r'(\s*[,\.]?\s*(д\.?|дом)?\s*\d+\s*[а-яА-Я]?)?'
    r'(\s*[,\.]?\s*(кв\.|квартира)?\s*\d+\s*[а-яА-Я]?)?'
)
tag = regex_tagger_factory(pattern)
