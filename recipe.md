# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def how_long_to_read(text, wpm:int=200):
    """takes a string text and estimates how long it would take to read at a pace of 200 words a minute (60 seconds)

    Parameters: 
        text: a string containing our text to be parsed
        wpm: an int defaulting to 200 as our baseline speed of words per minute

    Returns:
        a string with the format of 'Estimated reading time: {minutes_int} minute(s) and {seconds} second(s)'
    
    Side effects:
        this function shouldn't have any unexpected side effects
    """
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Estimate in minutes and seconds how long 
a string will take to be read @ 200 wpm
"""
how_long_to_read("This is a short example text that you might want to read quickly.") => "word_count/wpm minute(s) to read"

"""
Throw an error if given no text
"""
how_long_to_read("") => "Empty String, please enter some text"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python

fimport pytest
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
```

```python
def how_long_to_read(text, wpm=200):
    if text == "":
        raise Exception("Empty String, please enter some text")
    words = text.split()
    word_count = len(words)
    return f'{word_count/wpm} minute(s) to read'
```
Ensure all test function names are unique, otherwise pytest will ignore them!
