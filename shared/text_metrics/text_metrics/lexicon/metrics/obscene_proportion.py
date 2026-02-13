from text_metrics.core.context import DocumentContext
from text_metrics.lexicon.load_words import from_csv
from pathlib import Path

SOURCE_CSV = Path(__file__).parent.parent / "data" / "obscene.csv"
COLUMN_NAME = "Lemma"

if not SOURCE_CSV.exists():
    raise FileNotFoundError(f"Файл {SOURCE_CSV} с перечнем самых частых слов не найден")

obscene_words = from_csv(SOURCE_CSV, COLUMN_NAME)

METRIC_NAME = "obscene_proportion"
METRIC_GROUP = "text"

def extract(context: DocumentContext):
    lexicon = context.lexicon
    if not lexicon:
        return 0
    
    words = lexicon.keys()
    obscene = words & obscene_words
    
    obscene_count = sum([ lexicon[word] for word in obscene ])
    
    return obscene_count / lexicon.total()