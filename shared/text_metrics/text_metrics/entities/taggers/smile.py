from text_metrics.entities.base.regex_tag import regex_tagger_factory

TAG_NAME = "SMILE"

pattern = (
    r'('
    r'[:=;][-^~*]?[)dp(]+|'             # :) :-D ;P =(
    r'[)dp(]+[-^~*]?[:=;]|'             # D: )))): 
    r'[0o]_[0o]|'                       # 0_0 o_O
    r'[><t^][-_^][><t^]|'               # >_< ^_^ T_T
    r'x[dpo]+|'                         # xd xD
    r'[-\\/][_:][-\\/]|'                # -/- :-/
    r'[\[\]][-_][\[\]]|'                # :-[ ]-:
    r'\b((хи)+х?|(хе)+х?|(ха)+х?)\b'    # хихи хехе хахах
    r')'
)

tag = regex_tagger_factory(pattern)
