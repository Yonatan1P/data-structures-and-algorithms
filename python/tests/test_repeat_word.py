from challenges.repeated_word.repeated_word import repeat_word

def test_no_string():
    string=''
    actual = repeat_word(string)
    expected = False
    assert actual == expected

def test_no_repeats():
    string='Hi, my name is Yoni and I like toast!'
    actual = repeat_word(string)
    expected = False
    assert actual == expected

def test_one_repeats():
    string='Hi, I am Yoni and I like toast!'
    actual = repeat_word(string)
    expected = 'I'
    assert actual == expected
