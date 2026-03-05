from pathlib import Path
from .entities.TaggerLoader import TaggerLoader
from .metrics.loader import load_by_directories
from .documents.doc import extract_metrics

tagger_names = [
    "email",
    "url",
    "hashtag",
    "phone",
    "address_re",
    "address_natasha",
    "date_re",
    "date_natasha",
    "time"
    "measurement_natasha",
    "measurement_re",
    "enum",
    "number",
    "pointer",
    "quote", 
    "smile",
    "punct_emotion",
    "foreign",
]

taggers = TaggerLoader().load_by_tagger_names(tagger_names)

metric_dirs = [
    "./documents/metrics",
    "./entities/metrics",
    "./lexicon/metrics",
    "./pos/metrics",
    "./punct/metrics"
]

base_dir = Path(__file__).parent.resolve()

metric_paths = [ (base_dir / Path(p)).resolve() for p in metric_dirs ]

metrics = load_by_directories(metric_paths)

def extract(text):
    text = text.replace("ё", "е")
    
    return extract_metrics(text, taggers, metrics)
    
def flat_metrics(metrics):
    flattened_metrics = {}
    for category, m in metrics.items():
        for metric, value in m.items():
            column_name = f"{category}__{metric}"
            flattened_metrics[column_name] = value
            
    return flattened_metrics