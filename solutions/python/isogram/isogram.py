def is_isogram(phrase):
    letters = [char for char in phrase.lower() if char.isalpha()]
    return len(letters) == len(set(letters))
