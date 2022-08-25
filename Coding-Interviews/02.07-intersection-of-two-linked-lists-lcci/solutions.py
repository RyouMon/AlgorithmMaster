class Solution:
    """面试题 02.07. 链表相交"""

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA = 0
        cur = headA
        while cur:
            cur = cur.next
            lengthA += 1

        lengthB = 0
        cur = headB
        while cur:
            cur = cur.next
            lengthB += 1

        if lengthA > lengthB:
            long = headA
            short = headB
        else:
            long = headB
            short = headA

        for _ in range(abs(lengthA - lengthB)):
            long = long.next

        while long:
            if long is short:
                return long
            long = long.next
            short = short.next
        
        return None
