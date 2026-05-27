from src.extractors.known_sites.ramilevi_extractor import RamiLevyExtractor
from src.extractors.known_sites.superpharm_extractor import SuperPharmExtractor
from src.extractors.known_sites.babysitter_extractor import BabySitterExtractor



EXTRACTOR_REGISTRY = {
    "super-pharm.co.il":SuperPharmExtractor(),
    "baby-sitter.co.il":BabySitterExtractor(),
    "rami-levy.co.il":RamiLevyExtractor(),
}