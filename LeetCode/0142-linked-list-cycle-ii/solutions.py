class Solution:
    """142. 环形链表 II"""
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is slow:
                index1 = head
                index2 = fast
                while index1 is not index2:
                    index1 = index1.next
                    index2 = index2.next
                return index2

        return None
