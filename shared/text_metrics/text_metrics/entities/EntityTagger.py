from typing import List
from ..core.span import SpanTree, Span
from text_metrics.core.tagger import Tagger

class EntityTagger:
    def __init__(self, taggers: List[Tagger]):
        self._taggers = taggers
        self._tree = None

    def is_contains(self, start, end):
        if not self._tree: 
            return False

        return self._tree.overlap(start, end)

    def get_entities(self) -> List[Span]:
        if not self._tree: 
            return []
        
        return [ Span(span.start, span.end, span.data) for span in self._tree.get_spans() ]

    def tag(self, text):
        self._tree = SpanTree()

        for tagger in self._taggers:
            name = tagger.name
            spans = tagger.tag_func(text)

            for span in spans:
                _ = self._tree.try_add(span.start, span.end, { "entity": name } | span.data )
                
                # if not added: 
                    # print(f"{text[0:20]}. Сущность {name} не выделена {text[span.start:span.end]} ({span.start}:{span.end}). Причина: Интервал занят")
    