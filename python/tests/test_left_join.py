from challenges.hashtable.hashtable import Hashtable
from challenges.left_join.left_join import left_join

def test_happy_path():
    hashmap1 = Hashtable()
    hashmap1.add('Hello', 'Hi')
    hashmap1.add('Up', 'Above')
    hashmap1.add('Down', 'Below')
    hashmap1.add('Hot', 'Warm')

    hashmap2 = Hashtable()
    hashmap2.add('Hello', 'Bye')
    hashmap2.add('Up', 'Below')
    hashmap2.add('Down', 'Above')

    actual = left_join(hashmap1,hashmap2)
    expected = [
        ['Hello', 'Hi', 'Bye'],
        ['Up', 'Above', 'Below'],
        ['Down', 'Below', 'Above'],
        ['Hot', 'Warm', 'Null']
    ]
    assert actual == expected

def test_empty_left():
    hashmap1 = Hashtable()

    hashmap2 = Hashtable()
    hashmap2.add('Hello', 'Bye')
    hashmap2.add('Up', 'Below')
    hashmap2.add('Down', 'Above')

    actual = left_join(hashmap1,hashmap2)
    expected = []
    assert actual == expected

def test_empty_right():
    hashmap1 = Hashtable()

    hashmap2 = Hashtable()
    hashmap2.add('Hello', 'Bye')
    hashmap2.add('Up', 'Below')
    hashmap2.add('Down', 'Above')

    actual = left_join(hashmap2,hashmap1)
    expected = [
        ['Hello', 'Bye', 'Null'],
        ['Up', 'Below', 'Null'],
        ['Down', 'Above', 'Null']
    ]
    assert actual == expected
