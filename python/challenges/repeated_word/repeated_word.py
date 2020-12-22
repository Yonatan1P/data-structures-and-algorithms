from challenges.hashtable.hashtable import Hashtable

def repeat_word(string):
    if not string:
        return False
    words = string.split(' ')
    table = Hashtable()
    for word in words:
        word.lower()
        if table.contains(word):
            return word
        table.add(word, word)
    return False


