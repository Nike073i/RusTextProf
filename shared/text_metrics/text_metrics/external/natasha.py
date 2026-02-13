from natasha import MorphVocab, NewsEmbedding, NewsMorphTagger, Segmenter, Doc, AddrExtractor, MoneyExtractor, DatesExtractor

segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)

def create_doc(text) -> Doc:
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
    return doc

addr_extractor = AddrExtractor(morph_vocab)
money_extractor = MoneyExtractor(morph_vocab)
dates_extractor = DatesExtractor(morph_vocab)