from typing import Dict, List
from collections import Counter
from .span import Span

class DocumentStat:
    symbols_length: int
    
    def __init__(self, symbols_length):
        self.symbols_length = symbols_length
        

class EntitiesStat:
    spans: Dict[str, List[Span]]
    entities_width: int 
    
    def __init__(self, spans, entities_width):
        self.spans = spans
        self.entities_width = entities_width
        
    
class PosStat:
    seqs: List[List[Span]]
    sentences_count: int    
    
    def __init__(self, seqs):
        self.seqs = seqs
        self.sentences_count = len(seqs)
        
    def get_series(self, seq_start: Span = None, seq_end: Span = None):
        for seq in self.seqs:
            if seq_start:
                yield seq_start
            
            yield from seq
            
            if seq_end:
                yield seq_end
            

class DocumentContext:
    lexicon: Counter
    document_stat: DocumentStat
    entities: EntitiesStat
    pos: PosStat

    def __init__(self, lexicon: Counter, document_stat: DocumentStat, entities: EntitiesStat, pos: PosStat):
       self.lexicon = lexicon
       self.document_stat = document_stat 
       self.entities = entities
       self.pos = pos
