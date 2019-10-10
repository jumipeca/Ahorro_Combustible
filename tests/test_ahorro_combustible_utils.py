import gzip
import json
from ahorro_combustible import utils

def test_count_brands():
    with gzip.open('data/precios-gasolineras.json.gz') as f:
        result = utils.count_brands(json.load(f))[:5]
        assert result == [
            (2698, "REPSOL"),
            (1368, "CEPSA"),
            ( 515, "GALP"),
            ( 374, "SHELL"),
            ( 212, "BP")
        ]