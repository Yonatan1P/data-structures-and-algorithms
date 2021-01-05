from challenges.anagram.anagram import check_anagram

def test_normal_anagram():
    string1 = "Astronomers"
    string2 = "Moon starers"
    actual = check_anagram(string1,string2)
    expected = True
    assert actual == expected

def test_another_anagram():
    string1 = "Eleven plus two"
    string2 = "Twelve plus one"
    actual = check_anagram(string1,string2)
    expected = True
    assert actual == expected

def test_yet_another_anagram():
    string1 = "Clint Eastwood"
    string2 = "Old West Action"
    actual = check_anagram(string1,string2)
    expected = True
    assert actual == expected

def test_not_anagram():
    string1 = "Software"
    string2 = "Swear often"
    actual = check_anagram(string1,string2)
    expected = False
    assert actual == expected
