import pytest

from src.rate_note import rate_note


@pytest.mark.parametrize("note",[7,8,9])
def test_rate_note_is_unsuccessful(note):
    assert rate_note(note)=="unsuccessful"


@pytest.mark.parametrize("note",[10,11])
def test_rate_note_is_acceptable(note):
    assert rate_note(note)=="acceptable"

@pytest.mark.parametrize("note",[12,13])
def test_rate_note_is_good(note):
    assert rate_note(note)=="good"
def test_rate_note_14_is_very_good():
    assert rate_note(14)=="very good"
def test_rate_note_16_is_excellent():
    assert rate_note(16)=="excellent"
def test_rate_note_17_is_excellent():
    assert rate_note(17)=="excellent"


