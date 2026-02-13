from typing import Callable, List
from .span import Span

class Tagger:
    name: str
    tag_func: Callable[[str], List['Span']]

    def __init__(self, name, tag_func):
        self.name = name
        self.tag_func = tag_func