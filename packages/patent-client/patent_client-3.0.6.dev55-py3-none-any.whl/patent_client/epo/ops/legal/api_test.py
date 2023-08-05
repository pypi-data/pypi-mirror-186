import json
from pathlib import Path

from patent_client.util.test import compare_dicts

from .api import LegalApi

test_dir = Path(__file__).parent / "test"
expected_dir = Path(__file__).parent / "test" / "expected"


def test_example():
    result = LegalApi.get_legal("EP1000000A1")
    expected_file = expected_dir / "example.json"
    # expected_file.write_text(result.to_json(indent=2))
    expected = json.loads(expected_file.read_text())
    compare_dicts(json.loads(result.to_json()), expected)
