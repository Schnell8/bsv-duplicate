import pytest
from src.util.detector import detect_duplicates

# develop your test cases here

@pytest.mark.unit
def test_detect_duplicates():
    assert True

# Utility to build BibTeX strings with variations
def build_bibtex_entry(key, doi=None):
    entry = f"@article{{{key},\n  title={{Sample Title}},\n  author={{John Doe}},\n  year={{2020}},\n"
    if doi:
        entry += f"  doi={{ {doi} }},\n"
    entry += "  journal={Journal of Testing}\n}"
    return entry

@pytest.mark.unit
def test_1_duplicate_key_and_matching_doi():
    """TC1: key = yes, DOI = match → Duplicate"""
    entry1 = build_bibtex_entry("ref1", "10.1000/test")
    entry2 = build_bibtex_entry("ref1", "10.1000/test")
    data = entry1 + "\n\n" + entry2
    result = detect_duplicates(data)
    assert len(result) == 1

