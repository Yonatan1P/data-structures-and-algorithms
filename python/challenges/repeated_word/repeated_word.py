from challenges.hashtable.hashtable import Hashtable


def repeat_word(string):

    if not string:
        return False

    words = string.split(' ')
    table = Hashtable()

    for word in words:

        isolated_word = ""
        for char in word:
            if char != "," and char != "." and  char != "!" and char != "?" and char != "(" and char != ")"  and char != ":" and char != ";":
                isolated_word += char
        lower_case_word = isolated_word.lower()
        if table.contains(lower_case_word):
            return isolated_word
        table.add(lower_case_word, lower_case_word)
    return False
