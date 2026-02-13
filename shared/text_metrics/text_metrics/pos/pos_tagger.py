from ..core.span import Span

def __get_feat(token, feature):
    return token.feats.get(feature, "None")

def __get_code(token):
    pos = token.pos
    
    code = pos
    
    if pos == "ADJ":
        code = f"ADJ-{__get_feat(token, 'Degree')}"
    elif pos == "PART":
        code = f"PART-{__get_feat(token, 'Polarity')}"
    elif pos == "VERB":
        verb_form = __get_feat(token, "VerbForm")
        voice = __get_feat(token, "Voice")
        tense = __get_feat(token, "Tense")
        code = f"VERB-{verb_form}-{voice}-{tense}"
    
    return code

def __get_span(token):
    pos = token.pos
    code = __get_code(token)
    
    return Span(token.start, token.stop, { "pos": pos, "code": code, "text": token.text })

def tag(doc, entity_tagger):
    seqs = []
    lemms = []
    for sent in doc.sents:
        spans = []
        for token in sent.tokens:
            if not entity_tagger.is_contains(token.start, token.stop):
                spans.append(__get_span(token))
                lemms.append(token.lemma)
        
        seqs.append(spans)
    
    return seqs, lemms