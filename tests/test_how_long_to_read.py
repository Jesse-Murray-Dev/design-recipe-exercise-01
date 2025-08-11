from lib.how_long_to_read import *

def test_how_long_to_read_with_short_text():
    assert how_long_to_read("This is a short example text that you might want to read quickly.") == "Estimated reading time: 0 minute(s) and 3 second(s)"

def test_how_long_to_read_with_long_text():
    assert how_long_to_read("It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters.") == "Estimated reading time: 0 minute(s) and 21 second(s)"

def test_how_long_to_read_empty_text():
    assert how_long_to_read("") == "Empty String, please enter some text"