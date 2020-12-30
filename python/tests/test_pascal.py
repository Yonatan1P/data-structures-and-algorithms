from challenges.pascals.pascals import printPascal

def test_print_four_lines():
    actual = printPascal(4)
    expected = [[1], [1,1], [1,2,1], [1,3,3,1]]
    assert actual == expected

def test_string_input():
    actual = printPascal("n")
    expected = None
    assert actual == expected

def test_no_lines():
    actual = printPascal(0)
    expected = []
    assert actual == expected

def test_no_input():
    actual = printPascal()
    expected = []
    assert actual == expected

def test_non_integer():
    actual = printPascal(10.1)
    expected = None
    assert actual == expected
