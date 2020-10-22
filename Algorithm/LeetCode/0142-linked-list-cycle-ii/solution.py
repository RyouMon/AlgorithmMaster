# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:

        fast = head
        slow = head

        while (fast is not None) and (fast.next is not None):

            # 快指针每次前进两次，慢指针每次前进一次
            fast = fast.next.next
            slow = slow.next

            # 如果相遇则证明链表有环
            if fast is slow:
                p = head
                while p is not slow:
                    p = p.next
                    slow = slow.next
                return p

        return None
