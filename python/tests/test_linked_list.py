
from challenges.linked_list.linked_list import LinkedList
from code_challenges.reverse_linked_list import reverseLinkedList

def test_empty_list():
    assert LinkedList()


def test_insert():
    current_list = LinkedList()
    current_list.insert("first_node_added")
    current_list.insert("second_node_added")
    assert current_list.head.value == "second_node_added"
    assert current_list.head.next_node.value == "first_node_added"


def test_head_property():
    current_list = LinkedList()
    current_list.insert("fifth_node")
    current_list.insert("fourth_node")
    current_list.insert("third_node")
    current_list.insert("second_node")
    current_list.insert("first_node")
    assert current_list.head.value == "first_node"


def test_insert_multiple():
    current_list = LinkedList()
    current_list.insert("fifth_node")
    current_list.insert("fourth_node")
    current_list.insert("third_node")
    current_list.insert("second_node")
    current_list.insert("first_node")
    assert current_list.head.next_node.value == "second_node"


def test_true_includes():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(3)
    assert current_list.includes(2) == True


def test_false_includes():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(3)
    assert current_list.includes(10) == False


def test_str():
    current_list = LinkedList()
    current_list.insert("Tree")
    current_list.insert("The")
    current_list.insert("Up")
    current_list.insert("Climbed")
    current_list.insert("Cat")
    current_list.insert("The")
    actual = current_list.__str__()
    expected = "{ The } -> { Cat } -> { Climbed } -> { Up } -> { The } -> { Tree } -> NULL"
    assert actual == expected


def test_append_one_node():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(3)
    current_list.append(4)
    actual = current_list.__str__()
    expected = "{ 3 } -> { 2 } -> { 1 } -> { 4 } -> NULL"
    assert actual == expected


def test_append_multiple_nodes():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(3)
    current_list.append(4)
    current_list.append(4)
    current_list.append(4)
    actual = current_list.__str__()
    expected = "{ 3 } -> { 2 } -> { 1 } -> { 4 } -> { 4 } -> { 4 } -> NULL"
    assert actual == expected


def test_insert_before():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(1)
    current_list.insert(1)
    current_list.insert(1)
    current_list.insert_before(2, 3)
    actual = current_list.__str__()
    expected = "{ 1 } -> { 1 } -> { 1 } -> { 3 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected


def test_insert_before_everything():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(1)
    current_list.insert(1)
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert_before(2, 3)
    actual = current_list.__str__()
    expected = "{ 3 } -> { 2 } -> { 1 } -> { 1 } -> { 1 } -> { 1 } -> NULL"
    assert actual == expected


def test_insert_after_first_node():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(1)
    current_list.insert(1)
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert_after(2, 3)
    actual = current_list.__str__()
    expected = "{ 2 } -> { 3 } -> { 1 } -> { 1 } -> { 1 } -> { 1 } -> NULL"
    assert actual == expected


def test_insert_after_middle_node():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(1)
    current_list.insert(1)
    current_list.insert_after(2, 3)
    actual = current_list.__str__()
    expected = "{ 1 } -> { 1 } -> { 2 } -> { 3 } -> { 1 } -> { 1 } -> NULL"
    assert actual == expected


def test_count_from_end_great_than_length():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(3)
    current_list.insert(4)
    current_list.insert(5)
    actual = current_list.count_from_end(10)
    expected = "Exception"
    assert actual == expected


def test_count_from_end_equal_to_length():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(3)
    current_list.insert(4)
    current_list.insert(5)
    actual = current_list.count_from_end(5)
    expected = "Exception"
    assert actual == expected


def test_count_from_end_not_positive_integer():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(3)
    current_list.insert(4)
    current_list.insert(5)
    actual = current_list.count_from_end(-2)
    expected = "Exception"
    assert actual == expected


def test_count_from_end_length_of_one():
    current_list = LinkedList()
    current_list.insert(1)
    actual = current_list.count_from_end(0)
    expected = 1
    assert actual == expected


def test_count_from_end_properly():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(3)
    current_list.insert(4)
    current_list.insert(5)
    actual = current_list.count_from_end(2)
    expected = 3
    assert actual == expected

def test_reverse_linked_list():
    current_list = LinkedList()
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(3)
    current_list.insert(4)
    current_list.insert(5)
    actual = reverseLinkedList(current_list)
    expected = 1
    assert actual == expected
