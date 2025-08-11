import pytest
from lib.how_long_to_read import *

def test_how_long_to_read_100_words():
    text = " ".join(["word" for i in range(0, 100)])
    assert how_long_to_read(text) == "0.5 minute(s) to read"

def test_how_long_to_read_200_words():
    text = " ".join(["word" for i in range(0, 200)])
    assert how_long_to_read(text) == "1.0 minute(s) to read"

def test_how_long_to_read_with_very_long_text():
    text = " ".join(["word" for i in range(0, 500)])
    assert how_long_to_read(text) == "2.5 minute(s) to read"

def test_how_long_to_read_empty_text():
    with pytest.raises(Exception) as e:
        how_long_to_read("")
    assert str(e.value) == "Empty String, please enter some text"