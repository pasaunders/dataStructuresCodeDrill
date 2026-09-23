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

