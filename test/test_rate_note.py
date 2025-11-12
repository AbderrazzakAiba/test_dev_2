import pytest

from src.rate_note import rate_note


@pytest.mark.parametrize("note",[0,1,2,3,4,5,6,7,8,9])
def test_rate_note_is_unsuccessful(note):
    assert rate_note(note)=="unsuccessful"


@pytest.mark.parametrize("note",[10,11])
def test_rate_note_is_acceptable(note):
    assert rate_note(note)=="acceptable"

@pytest.mark.parametrize("note",[12,13])
def test_rate_note_is_good(note):
    assert rate_note(note)=="good"


@pytest.mark.parametrize("note",[14,15])
def test_rate_note_is_very_good(note):
    assert rate_note(note)=="very good"

@pytest.mark.parametrize("note",[16,17,18,19,20])
def test_rate_note_is_excellent(note):
    assert rate_note(note)=="excellent"




