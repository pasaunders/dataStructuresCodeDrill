from linked_list import LinkedList
from collections.abc import Iterable
from typing import Any

class Stack(object):
    """class representation of a stack"""

    def __init__(self, values: Iterable | None = None):
        """instantiate stack"""
        self.linked_list = LinkedList(values)
        self.head = self.linked_list.head

    def push(self, val: Any) -> None:
        """add node to this stack"""
        self.linked_list.push(val)
        self.head = self.linked_list.head

    def pop(self) -> Any:
        """remove and return the head node"""
        old_head = self.linked_list.pop
        self.head = self.linked_list.head
        return old_head
