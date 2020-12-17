from challenges.quick_sort.quick_sort import quick_sort


def test_normal_quick_sort():
    arr = [8, 4, 23, 42, 16, 15]
    left = 0
    right = 5
    quick_sort(arr, left, right)
    actual = arr
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_reverse_quick_sort():
    arr = [20, 18, 12, 8, 5, -2]
    left = 0
    right = 5
    quick_sort(arr, left, right)
    actual = arr
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_duplicates_quick_sort():
    arr = [5, 12, 7, 5, 5, 7]
    left = 0
    right = 5
    quick_sort(arr, left, right)
    actual = arr
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_nearly_sorted_quick_sort():
    arr = [2, 3, 5, 7, 13, 11]
    left = 0
    right = 5
    quick_sort(arr, left, right)
    actual = arr
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
