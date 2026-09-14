from __future__ import annotations
from collections.abc import Iterable
from typing import Any

class LinkedList:
    """ Class representation of a LinkedList"""

    def __init__(self, values: Iterable | None = None) -> None:
        self.head = None
        self.length = 0
        try:
            for item in values:
                self.push(item)
        except TypeError:
            print("values must be iterable or None")

    def push(self, value: Any | None = None) -> None:
        self.head = Node(value, self.head)
        self.length += 1

    def pop(self) -> Node | None:
        """remove and return the head node"""
        if not self.head:
            return None
        old_head = self.head
        self.head = self.head.next
        self.length -= 1
        return old_head

    def search(self, search_val: Any | None = None) -> Node | None:
        """return the first node with a matching value"""
        if self.head is None:
            return None
        matching_node = self.head
        while matching_node.val is not search_val:
            matching_node = matching_node.next
            if matching_node.next is None: return None
        return matching_node


class Node:
    """Singly linked node containing a value and pointer to another node"""
    def __init__(self, val: Any | None = None, next: Node | None = None) -> None:
        self.val = val
        self.next = next