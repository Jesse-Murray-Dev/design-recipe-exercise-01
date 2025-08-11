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