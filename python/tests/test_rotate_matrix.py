from challenges.rotate_matrix.rotate_matrix import rotate_clockwise

def test_normal_matrix():

    matrix = [ [1, 1, 1], [2, 2, 2], [3, 3, 3] ]
    actual = rotate_clockwise(matrix)
    expected = [ [3, 2, 1], [3, 2, 1], [3, 2, 1] ]
    assert actual == expected

def test_another_matrix():

    matrix = [ [3, 2, 1], [3, 2, 1], [3, 2, 1] ]
    actual = rotate_clockwise(matrix)
    expected = [ [3, 3, 3], [2, 2, 2], [1, 1, 1] ]
    assert actual == expected
