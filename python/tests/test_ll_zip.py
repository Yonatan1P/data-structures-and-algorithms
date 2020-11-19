import pytest
from challenges.ll_zip.ll_zip import LinkedList, zip_lists

def test_zip_lists_happy():
    list_1 = LinkedList()
    list_1.insert("5")
    list_1.insert("4")
    list_1.insert("3")
    list_1.insert("2")
    list_1.insert("1")
    list_2 = LinkedList()
    list_2.insert("E")
    list_2.insert("D")
    list_2.insert("C")
    list_2.insert("B")
    list_2.insert("A")
    actual = zip_lists(list_1,list_2)
    expected = "{ 1 } -> { A } -> { 2 } -> { B } -> { 3 } -> { C } -> { 4 } -> { D } -> { 5 } -> { E } -> NULL"
    assert actual == expected

def test_zip_list_no_lists():
    list_1 = LinkedList()
    list_2 = LinkedList()
    actual = zip_lists(list_1,list_2)
    expected = "NULL"
    assert actual == expected


def test_zip_lists_first_longer():
    list_1 = LinkedList()
    list_1.insert("5")
    list_1.insert("4")
    list_1.insert("3")
    list_1.insert("2")
    list_1.insert("1")
    list_2 = LinkedList()
    list_2.insert("C")
    list_2.insert("B")
    list_2.insert("A")
    actual = zip_lists(list_1,list_2)
    expected = "{ 1 } -> { A } -> { 2 } -> { B } -> { 3 } -> { C } -> { 4 } -> { 5 } -> NULL"
    assert actual == expected

@pytest.mark.skip('pending')
def test_zip_lists_second_longer():
    list_1 = LinkedList()
    list_1.insert("3")
    list_1.insert("2")
    list_1.insert("1")
    list_2 = LinkedList()
    list_2.insert("E")
    list_2.insert("D")
    list_2.insert("C")
    list_2.insert("B")
    list_2.insert("A")
    actual = zip_lists(list_1,list_2)
    expected = "{ 1 } -> { A } -> { 2 } -> { B } -> { 3 } -> { C } -> { D } -> { E } -> NULL"
    assert actual == expected

