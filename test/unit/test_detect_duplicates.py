import pytest
from src.util.detector import detect_duplicates

# Build BibTeX strings with variations
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

#@pytest.mark.unit
#def test_2_duplicate_key_different_doi():
#    """TC2: key = yes, DOI = differ → Not duplicate"""
#    entry1 = build_bibtex_entry("ref1", "10.1000/a")
#    entry2 = build_bibtex_entry("ref1", "10.1000/b")
#    data = entry1 + "\n\n" + entry2
#    result = detect_duplicates(data)
#    assert len(result) == 0

@pytest.mark.unit
def test_3_duplicate_key_missing_doi():
    """TC3: key = yes, one DOI missing → Duplicate"""
    entry1 = build_bibtex_entry("ref1", "10.1000/test")
    entry2 = build_bibtex_entry("ref1", None)
    data = entry1 + "\n\n" + entry2
    result = detect_duplicates(data)
    assert len(result) == 1

@pytest.mark.unit
def test_4_different_key_matching_doi():
    """TC4: key = no, DOI = match → Not duplicate"""
    entry1 = build_bibtex_entry("ref1", "10.1000/test")
    entry2 = build_bibtex_entry("ref2", "10.1000/test")
    data = entry1 + "\n\n" + entry2
    result = detect_duplicates(data)
    assert len(result) == 0

@pytest.mark.unit
def test_5_different_key_different_doi():
    """TC5: key = no, DOI = differ → Not duplicate"""
    entry1 = build_bibtex_entry("ref1", "10.1000/a")
    entry2 = build_bibtex_entry("ref2", "10.1000/b")
    data = entry1 + "\n\n" + entry2
    result = detect_duplicates(data)
    assert len(result) == 0

@pytest.mark.unit
def test_6_different_key_missing_doi():
    """TC6: key = no, both DOI missing → Not duplicate"""
    entry1 = build_bibtex_entry("ref1", None)
    entry2 = build_bibtex_entry("ref2", None)
    data = entry1 + "\n\n" + entry2
    result = detect_duplicates(data)
    assert len(result) == 0

# The test cases are structured based on a test design table using the four-step method.
# Each test targets a specific combination of conditions involving BibTeX key matching and DOI presence.
# A helper function (build_bibtex_entry) is used to generate consistent input data for each test case.

# Each test function is self-contained and builds its own BibTeX input data.
# There is no shared state, no reliance on global variables, and tests do not affect one another.

# Simulating realistic BibTeX input including proper formatting and line separation to ensure the parser function handled input correctly during tests.