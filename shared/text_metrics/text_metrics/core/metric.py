from typing import Callable, Dict, Union, Optional, Protocol
from .context import DocumentContext

class Metric(Protocol):
    name: Optional[str]
    group: Optional[str]
    extract_func: Callable[[DocumentContext], Union[Dict, float]]

    def __init__(self, name, group, extract_func):
        self.name = name
        self.group = group
        self.extract_func = extract_func