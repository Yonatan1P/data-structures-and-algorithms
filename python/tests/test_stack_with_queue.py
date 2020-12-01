from challenges.queue_with_stacks.queue_with_stacks import PsuedoQueue


def test_enqueue_into_empty_PsuedoQueue():
    queue = PsuedoQueue()
    queue.enqueue(1)
    actual = queue.top.value
    expected = 1
    assert actual == expected


def test_multiple_enqueue_into_PsuedoQueue():
    queue = PsuedoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.top.value
    expected = 1
    assert actual == expected


def test_dequeue_from_PsuedoQueue():
    queue = PsuedoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.dequeue()
    expected = 1
    assert actual == expected


def test_multiple_dequeue_from_PsuedoQueue():
    queue = PsuedoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    actual = queue.dequeue()
    expected = 3
    assert actual == expected


def test_dequeue_from_empty_PsuedoQueue():
    queue = PsuedoQueue()
    actual = queue.dequeue()
    expected = None
    assert actual == expected
