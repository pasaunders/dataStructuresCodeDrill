import pytest
from stack import Stack

@pytest.fixture
def sample_one_stack():
    return Stack([1])

@pytest.fixture
def sample_empty_stack():
    return Stack([])

@pytest.fixture
def sample_filled_stack():
    return Stack([1,2,3,4,5])

def test_stack_empty_head(sample_empty_stack):
    assert sample_empty_stack.head is None

def test_stack_new_contents(sample_filled_stack):
    assert sample_filled_stack.head.val == 5
    assert sample_filled_stack.head.next.val == 4
    assert sample_filled_stack.head.next.next.val == 3
    assert sample_filled_stack.head.next.next.next.val == 2
    assert sample_filled_stack.head.next.next.next.next.val == 1

def test_stack_new_push(sample_filled_stack):
    sample_filled_stack.push(34)
    assert sample_filled_stack.head.val == 34

def test_stack_empty_push(sample_empty_stack):
    sample_empty_stack.push(34)
    assert sample_empty_stack.head.val == 34

def test_stack_pop(sample_filled_stack):
    assert sample_filled_stack.pop().val == 5

def test_stack_one_pop(sample_one_stack):
    assert sample_one_stack.pop().val == 1
    assert sample_one_stack.head is None

def test_stack_empty_pop(sample_empty_stack):
    assert sample_empty_stack.pop() is None