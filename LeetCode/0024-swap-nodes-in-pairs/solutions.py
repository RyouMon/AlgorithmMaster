class Solution:
    """24. 两两交换链表中的节点"""
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(next=head)
        cur = dummyHead

        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            third = cur.next.next.next

            cur.next = second
            second.next = first
            first.next = third

            cur = cur.next.next

        return dummyHead.next
