from cachetools import cached, TTLCache
from hashlib import sha256
from ...domain.text import extract_metrics


text_cache = TTLCache(maxsize=1000, ttl=10*60)

@cached(text_cache, key=lambda text: sha256(text.encode()).hexdigest())
def cached_get_metrics(text):
    return extract_metrics(text)

async def async_get_metrics(text):
    return cached_get_metrics(text)
