from challenges.hashtable.hashtable import Hashtable

def test_create_hashtable():
    assert Hashtable()

def test_add_key():
    hashtable = Hashtable()
    hashtable.add('hi','my name is WHO')
    assert hashtable._buckets[hashtable._hash('hi')]

def test_get_value():
    table = Hashtable()
    table.add('hey','my name is WHERE')
    actual = table.get('hey')
    expected = 'my name is WHERE'
    assert actual == expected

def test_get_null_key():
    table = Hashtable()
    actual = table.get('hey')
    expected = 'Null'
    assert actual == expected

def test_handle_collision():
    table = Hashtable()
    table.add('hi', 'my name is WHAT')
    table.add('Ñ','my name is WHO')
    assert table._hash('Ñ') == table._hash('hi')

def test_get_second_in_bueket():
    table = Hashtable()
    table.add('hi', 'my name is WHAT')
    table.add('Ñ','my name is WHO')
    actual = table.get('Ñ')
    expected = 'my name is WHO'
    assert actual == expected

def test_contains():
    table = Hashtable()
    table.add('hi', 'my name is WHAT')
    assert table.contains('hi')

def test_add_key_in_range():
    table = Hashtable()
    table.add('hi', 'my name is WHAT')
    