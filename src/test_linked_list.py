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
    print
    assert sample_linked_list["one_llist"].length == 1