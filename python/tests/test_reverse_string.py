from challenges.reverse_string.reverse_string import reverse_string_array, reverse_string_recursive, reverse_string_stack

def test_reverse_string_array():
    string = "hi, how is it going?"
    actual = reverse_string_array(string)
    expected = "?gniog ti si woh ,ih"
    assert actual == expected

def test_empty_reverse_array():
    string =''
    actual = reverse_string_array(string)
    expected = ''
    assert actual == expected

def test_reverse_string_recursive():
    string = "hi, how is it going?"
    actual = reverse_string_recursive(string)
    expected = "?gniog ti si woh ,ih"
    assert actual == expected

def test_empty_reverse_recursive():
    string =''
    actual = reverse_string_recursive(string)
    expected = ''
    assert actual == expected

def test_reverse_string_stack():
    string = "hi, how is it going?"
    actual = reverse_string_stack(string)
    expected = "?gniog ti si woh ,ih"
    assert actual == expected

def test_empty_reverse_stack():
    string =''
    actual = reverse_string_stack(string)
    expected = ''
    assert actual == expected
