from challenges.fifo_animal_shelter.fifo_animal_shelter import Queue

def test_empty_shelter():
    shelter = Queue()
    actual = shelter.front
    expected = None
    assert actual == expected

def test_enqueue_once():
    shelter = Queue()
    shelter.enqueue("dog")
    actual = shelter.front.animal_type
    expected = "dog"
    assert actual == expected

def test_enqueue_multiple_dog_first():
    shelter = Queue()
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    actual = shelter.front.animal_type
    expected = "dog"
    assert actual == expected

def test_enqueue_multiple_cat_first():
    shelter = Queue()
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    actual = shelter.front.animal_type
    expected = "cat"
    assert actual == expected

def test_dequeue_from_empty():
    shelter = Queue()
    actual = shelter.dequeue("cat")
    expected = "No animals available"
    assert actual == expected


def test_dequeue_existing_cat():
    shelter = Queue()
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    actual = shelter.dequeue("cat")
    expected = "cat"
    assert actual == expected

def test_dequeue_invalid_preference():
    shelter = Queue()
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    actual = shelter.dequeue("pig")
    expected = "Null"
    assert actual == expected

def test_dequeue_missing_cat():
    shelter = Queue()
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    shelter.enqueue("dog")
    actual = shelter.dequeue("cat")
    expected = "Null"
    assert actual == expected
