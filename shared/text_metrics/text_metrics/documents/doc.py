from collections import Counter, defaultdict
from typing import List
from ..external.natasha import create_doc
from ..entities.EntityTagger import EntityTagger
from ..core.tagger import Tagger
from ..core.metric import Metric
from ..core.context import DocumentContext, DocumentStat, EntitiesStat, PosStat
from ..pos.pos_tagger import tag as pos_tag
from .MetricExtractor import MetricExtractor

def extract_metrics(text, taggers: List[Tagger], metrics: List[Metric]):
    entity_tagger = EntityTagger(taggers)
    entity_tagger.tag(text)
    entity_spans = entity_tagger.get_entities()
    
    entities = defaultdict(list)
    
    for span in entity_spans:
        entities[span.data['entity']].append(span)
    
    entities_width = len(set([ tagger.name for tagger in taggers ]))
    entities_stat = EntitiesStat(entities, entities_width)
    
    doc = create_doc(text)
    
    seqs, lemms = pos_tag(doc, entity_tagger)
    
    pos_stat = PosStat(seqs)

    lexicon = Counter(lemms)
    
    doc_stat = DocumentStat(len(text))
    
    context = DocumentContext(lexicon, doc_stat, entities_stat, pos_stat)

    metric_extractor = MetricExtractor(metrics)
    values = metric_extractor.extract(context)

    return values
