import pytest

@pytest.fixture
def sample_linked_list():
    """Create linked list for testing"""
    from linked_list import LinkedList
    return {"one_llist": LinkedList([1]),
            "empty_llist": LinkedList(),
            "new_llist": LinkedList([1,2,3,4,5])
            }

def test_node_init():
    """test node class init"""
    from linked_list import Node
    new_node = Node(0, None)
    assert new_node.val == 0 and new_node.next == None

def test_linkedlist_empty_size(sample_linked_list):
    assert sample_linked_list["empty_llist"].length == 0

def test_linkedlist_empty_head(sample_linked_list):
    assert sample_linked_list["empty_llist"].head == None

def test_linkedlist_init_one_size(sample_linked_list):
    assert sample_linked_list["one_llist"].length == 1

def test_linkedlist_init_list_size(sample_linked_list):
    assert sample_linked_list["new_llist"].length == 5

def test_linkedlist_init_list_head_expected_value(sample_linked_list):
    assert sample_linked_list["new_llist"].head.val == 5

def test_linkedlist_push(sample_linked_list):
    sample_linked_list["empty_llist"].push("a")
    assert sample_linked_list["empty_llist"].length == 1
    assert sample_linked_list["empty_llist"].head.val == "a"

def test_linkedlist_pop(sample_linked_list):
    assert sample_linked_list["new_llist"].pop().val == 5
    assert sample_linked_list["new_llist"].length == 4