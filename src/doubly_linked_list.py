from collections.abc import Iterable
from typing import Any, Self

class Node(object):
    """doubly linked list node"""
    def __init__(self, val: Any | None = None, next: Self | None = None, prev: Self | None = None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList(object):

    def __init__(self, iterable: Iterable | None = None):
        self.head = None
        self.tail = None
        self.length = 0
        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, value: Any | None) -> None:
        """Add value to new node at head"""
        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.head = Node(value, self.head)
            self.head.next.prev = self.head
        self.length += 1

    def append(self, value: Any | None) -> None:
        """add value to new node at tail"""
        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail = Node(value, None, self.tail)
        self.length += 1

    def pop(self) -> Node | None:
        """remove and return current head node"""
        pass

    def shift(self) -> Node | None:
        """remove and return the tail node"""
        pass

    def remove(self, val) -> None:
        pass

        