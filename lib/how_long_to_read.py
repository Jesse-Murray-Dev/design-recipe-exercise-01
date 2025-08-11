def how_long_to_read(text, wpm=200):
    if text == "":
        raise Exception("Empty String, please enter some text")
    words = text.split()
    word_count = len(words)
    return f'{word_count/wpm} minute(s) to read'