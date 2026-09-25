import pytest
from doubly_linked_list import DoublyLinkedList

@pytest.fixture
def sample_one_dll():
    return DoublyLinkedList([1])

@pytest.fixture
def sample_empty_dll():
    return DoublyLinkedList()

@pytest.fixture
def sample_filled_dll():
    return DoublyLinkedList([1,2,3,4,5])

def test_node_init():
    from doubly_linked_list import Node
    new_node = Node(0)
    assert new_node.val == 0
    assert new_node.prev == None
    assert new_node.next == None

def test_dll_init(sample_empty_dll):
    assert sample_empty_dll.length == 0
    assert sample_empty_dll.tail == None
    assert sample_empty_dll.head == None

def test_dll_init_filled(sample_filled_dll):
    assert sample_filled_dll.length == 5
    assert sample_filled_dll.tail.val == 1
    assert sample_filled_dll.head.val == 5

def test_dll_push(sample_filled_dll):
    sample_filled_dll.push(6)
    assert sample_filled_dll.length == 6
    assert sample_filled_dll.head.val == 6

def test_dll_append(sample_filled_dll, sample_empty_dll):
    sample_filled_dll.append(0)
    assert sample_filled_dll.length == 6
    assert sample_filled_dll.tail.val == 0
    sample_empty_dll.append(1)
    assert sample_empty_dll.length == 1
    assert sample_empty_dll.head.val == 1
    assert sample_empty_dll.tail.val == 1