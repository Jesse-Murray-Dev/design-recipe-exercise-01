# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def how_long_to_read(text, wpm:int=200) -> str:
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
how_long_to_read("This is a short example text that you might want to read quickly.") => 
    "Estimated reading time: 0 minute(s) and 2 second(s)"

"""
Throw an error if given no text
"""
how_long_to_read("") => "No text found, please enter text"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python

from lib.how_long_to_read import *

"""
Estimate in minutes and seconds how long 
a string will take to be read @ 200 wpm
"""
def test_how_long_to_read_with_short_text():
    assert how_long_to_read("This is a short example text that you might want to read quickly.") == "Estimated reading time: 0 minute(s) and 2 second(s)"

def test_how_long_to_read_with_long_text():
    assert how_long_to_read("It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters.") == "Estimated reading time: 0 minute(s) and 18 second(s)"

def test_how_long_to_read_with_very_long_text():
    assert how_long_to_read('It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters. "My dear Mr. Bennet," said his lady to him one day, "have you heard that Netherfield Park is let at last?" Mr. Bennet replied that he had not. "But it is," returned she; "for Mrs. Long has just been here, and she told me all about it." Mr. Bennet made no answer. "Do you not want to know who has taken it?" cried his wife impatiently. "You want to tell me, and I have no objection to hearing it." This was invitation enough. "Why, my dear, you must know, Mrs. Long says that Netherfield is taken by a young man of large fortune from the north of England; that he came down on Monday in a chaise and four to see the place, and was so much delighted with it that he agreed with Mr. Morris immediately; he is to take possession before Michaelmas, and some of his servants are to be in the house by the end of next week." Mr. Bennet sat silent. "You are not so easily moved, I see," said his wife with a sigh. "But I daresay you will like him very much."') == "Estimated reading time: 1 minute(s) and 17 second(s)"

def test_how_long_to_read_empty_text():
    assert how_long_to_read("") == "Empty String, please enter some text"
```

```python
def how_long_to_read(text, wpm=200):
    if text != "":
        words = text.split()
        word_count = len(words)
        minutes = word_count / wpm
        minutes_int = int(minutes)
        seconds = int((minutes - minutes_int) * 60)
        
        return f"Estimated reading time: {minutes_int} minute(s) and {seconds} second(s)"
    else:
        return "Empty String, please enter some text"
```
Ensure all test function names are unique, otherwise pytest will ignore them!
