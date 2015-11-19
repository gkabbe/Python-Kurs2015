def palindrom(word):
    word_reverse = reversed(word)
    for char1, char2 in zip(word, word_reverse):
        if char1 != char2:
            return False
    return True
    
def palindrom_rekursiv(word):
    if len(word) in (0, 1):
        return True
    else:
        return word[0] == word[-1] and palindrom_rekursiv(word[1:-1])
