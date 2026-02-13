from dataclasses import dataclass
from intervaltree import IntervalTree
from typing import List

@dataclass
class Span:
    start: int
    end: int
    data: object


class SpanTree:
    def __init__(self):
        self._tree = IntervalTree()

    def try_add(self, start, end, data):
        overlapping = self.overlap(start, end)
        if overlapping: return False

        self._tree.addi(start, end, data)
        return True
    
    def overlap(self, start, end):
        return self._tree.overlap(start, end)
    
    def get_spans(self) -> List[Span]:
        return [ Span(start, end, data) for (start, end, data) in self._tree ]