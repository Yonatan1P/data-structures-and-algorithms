from challenges.multi_bracket_validation.multi_bracket_validation import match_brackets


def test_empty_string():
    actual = match_brackets("")
    expected = True
    assert actual == expected


def test_unmatched_openner():
    actual1 = match_brackets("{")
    actual2 = match_brackets("(")
    actual3 = match_brackets("[")
    expected = False
    assert actual1 == expected
    assert actual2 == expected
    assert actual3 == expected


def test_unmatched_closer():
    actual1 = match_brackets("}")
    actual2 = match_brackets(")")
    actual3 = match_brackets("]")
    expected = False
    assert actual1 == expected
    assert actual2 == expected
    assert actual3 == expected


def test_proper_brackets():
    actual1 = match_brackets("{[()]}")
    actual2 = match_brackets("{}")
    actual3 = match_brackets("[]")
    actual4 = match_brackets("()")
    actual5= match_brackets("[(){}]")
    expected = True
    assert actual1 == expected
    assert actual2 == expected
    assert actual3 == expected
    assert actual4 == expected
    assert actual5 == expected
