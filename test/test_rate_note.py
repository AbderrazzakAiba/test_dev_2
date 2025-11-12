from src.rate_note import rate_note



def test_rate_note_9_is_unsuccessful():
    assert rate_note(9)=="unsuccessful"
def test_rate_note_10_is_acceptable():
    assert rate_note(10)=="acceptable"