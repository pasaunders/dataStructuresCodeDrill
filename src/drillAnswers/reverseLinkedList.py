class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseListRecursive(self, head: ListNode | None) -> ListNode | None:
        if not head or head.next:
            return head
        else:
            newNode = self.reverseListRecursive(head.next)
            head.next.next = head
            head.next = None
            return newNode

    def reverseListIterative(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev