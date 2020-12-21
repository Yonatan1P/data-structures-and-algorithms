import pytest

from challenges.stacks_and_queues.stacks_and_queues import Stack, InvalidOperationError, Queue

# Stack Tests
def test_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected


def test_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    actual = s.top.value
    expected = "cucumber"
    assert actual == expected


def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


def test_pop_some():
    s = Stack()

    s.push("apple")
    s.push("banana")
    s.push("cucumber")

    s.pop()

    actual = s.pop()
    expected = "banana"

    assert actual == expected


def test_check_not_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.is_empty()
    expected = False
    assert actual == expected

def test_pop_until_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected


def test_stack_peek():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.peek()
    expected = "banana"
    assert actual == expected


def test_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.peek()

    assert str(e.value) == "Method not allowed on empty collection"


def test_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.pop()

    assert str(e.value) == "Method not allowed on empty collection"

# Queue Tests

def test_enqueue():
    q = Queue()
    q.enqueue("apple")
    actual = q.front.value
    expected = "apple"
    assert actual == expected

def test_multiple_enqueue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("orange")
    q.enqueue("pineapple")
    q.enqueue("mango")
    actual1 = q.front.value
    expected1 = "apple"
    assert actual1 == expected1
    actual2 = q.rear.value
    expected2 = "mango"
    assert actual2 == expected2

def test_dequeue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual1 = q.dequeue()
    expected1 = "apple"
    assert actual1 == expected1
    actual2 = q.front.value
    expected2 = "banana"
    assert actual2 == expected2

def test_dequeue_empty_rear():
    q = Queue()
    q.enqueue("apple")
    q.dequeue()
    actual = q.rear
    expected = None
    assert actual == expected


def test_queue_peek():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.peek()
    expected = "apple"
    assert actual == expected


def test_peek_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.peek()


def test_enqueue_one():
    q = Queue()
    q.enqueue("apples")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


def test_enqueue_two():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


def test_dequeue_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.dequeue()


def test_dequeue_when_full():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


def test_peek_post_dequeue():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.peek()
    expected = "bananas"
    assert actual == expected


def test_is_empty():
    q = Queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected


def test_exhausted():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected
