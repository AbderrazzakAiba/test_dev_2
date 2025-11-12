import pytest

from src.rate_note import rate_note


@pytest.mark.parametrize("note",[7,8,9])
def test_rate_note_is_unsuccessful(note):
    assert rate_note(note)=="unsuccessful"

def test_rate_note_10_is_acceptable():
    assert rate_note(10)=="acceptable"
def test_rate_note_12_is_good():
    assert rate_note(12)=="good"
