from challenges.repeated_word.repeated_word import repeat_word


def test_no_string():
    string = ''
    actual = repeat_word(string)
    expected = False
    assert actual == expected


def test_no_repeats():
    string = 'Hi, my name is Yoni and I like toast!'
    actual = repeat_word(string)
    expected = False
    assert actual == expected


def test_one_repeats():
    string = 'Hi, I am Yoni and I like toast!'
    actual = repeat_word(string)
    expected = 'I'
    assert actual == expected


def test_multiple_repeats():
    string = 'Hi, my name is Yoni. And Yoni likes toast. And I am the person with the name Yoni, also I like toast!'
    actual = repeat_word(string)
    expected = 'Yoni'
    assert actual == expected

def test_first_sample():
    string ="Once upon a time, there was a brave princess who..."
    actual = repeat_word(string)
    expected = "a"
    assert actual == expected

def test_second_sample():
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = repeat_word(string)
    expected = "it"
    assert actual == expected

def test_third_sample():
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = repeat_word(string)
    expected = "summer"
    assert actual == expected
