from challenges.hashtable.hashtable import Hashtable


def repeat_word(string):
    if not string:
        return False
    words = string.split(' ')
    table = Hashtable()
    for word in words:

        saved_word = ''
        for char in word:
            if char != '.' and '!' and '?' and '(' and ')' and ',' and ':' and ';':
                saved_word += char
        lower_case_word = saved_word.lower()

        if table.contains(lower_case_word):
            return saved_word
        table.add(lower_case_word, lower_case_word)
    return False
