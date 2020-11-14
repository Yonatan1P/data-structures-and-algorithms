import pytest
from linked_list import LinkedList

def test_empty_list():
    assert LinkedList()

def test_insert():
    current_list=LinkedList()
    current_list.insert("first_node_added")
    current_list.insert("second_node_added")
    assert current_list.head.value == "second_node_added"
    assert current_list.head.next_node.value == "first_node_added"

def test_head_property():
    current_list=LinkedList()
    current_list.insert("fifth_node")
    current_list.insert("fourth_node")
    current_list.insert("third_node")
    current_list.insert("second_node")
    current_list.insert("first_node")
    assert current_list.head.value == "first_node"

def test_insert_multiple():
    current_list=LinkedList()
    current_list.insert("fifth_node")
    current_list.insert("fourth_node")
    current_list.insert("third_node")
    current_list.insert("second_node")
    current_list.insert("first_node")
    assert current_list.head.next_node.value == "second_node"

def test_true_includes():
    current_list=LinkedList()
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(3)
    assert current_list.includes(2)==True

def test_false_includes():
    current_list=LinkedList()
    current_list.insert(1)
    current_list.insert(2)
    current_list.insert(3)
    assert current_list.includes(10)==False

def test_str():
    current_list=LinkedList()
    current_list.insert("Tree")
    current_list.insert("The")
    current_list.insert("Up")
    current_list.insert("Climbed")
    current_list.insert("Cat")
    current_list.insert("The")
    actual = current_list.__str__()
    expected = "{The}->{Cat}->{Climbed}->{Up}->{The}->{Tree}->Null"
    assert actual == expected
