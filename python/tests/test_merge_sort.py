from challenges.merge_sort.merge_sort import merge_sort

def test_normal_merge_sort():
    arr = [1,3,2,5,4]
    merge_sort(arr)
    actual = arr
    expected = [1,2,3,4,5]
    assert actual == expected

def test_one_index_merge_sort():
    arr = [1]
    merge_sort(arr)
    actual = arr
    expected = [1]
    assert actual == expected

def test_no_index_merge_sort():
    arr = []
    merge_sort(arr)
    actual = arr
    expected = []
    assert actual == expected

def test_repeat_index_merge_sort():
    arr = [2,2,2,2,1]
    merge_sort(arr)
    actual = arr
    expected = [1,2,2,2,2]
    assert actual == expected

def test_negative_number_merge_sort():
    arr = [-1,-2,-3,-4,-5]
    merge_sort(arr)
    actual = arr
    expected = [-5,-4,-3,-2,-1]
    assert actual == expected
