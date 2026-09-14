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


class Node:
    """Singly linked node containing a value and pointer to another node"""
    def __init__(self, val: Any | None = None, next: Node | None = None) -> None:
        self.val = val
        self.next = next