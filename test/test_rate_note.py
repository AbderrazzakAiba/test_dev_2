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

@pytest.mark.parametrize("note",[16,17,18,19])
def test_rate_note_is_excellent(note):
    assert rate_note(note)=="excellent"


def test_rate_note_14_is_very_good():
    assert rate_note(14)=="very good"




