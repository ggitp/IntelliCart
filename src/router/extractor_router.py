
from src.router.extractor_registry import EXTRACTOR_REGISTRY

def get_extractor_for_url(url):
    for domain, extractor in EXTRACTOR_REGISTRY.items():
        if domain in url:
            return extractor

    return None