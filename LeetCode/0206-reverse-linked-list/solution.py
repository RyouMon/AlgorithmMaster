# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution01:
    """
    双指针法
    """

    def reverseList(self, head: ListNode) -> ListNode:

        # 设置两个指针
        pre = None
        cur = head

        # 依次反转 next 指针，直到 cur 指针指向 None
        while cur is not None:
            # 保存 cur 的下一个节点，并更新 cur.next
            tmp = cur.next
            cur.next = pre
            # 更新两个指针
            pre = cur
            cur = tmp
        # 最后 pre 指针就是新链表的头节点
        return pre


class Solution02:
    """
    递归法
    """

    def reverseList(self, head: ListNode) -> ListNode:

        cur = head
        pre = None
        return self.reverse(cur, pre)

    def reverse(self, cur, pre) -> ListNode:
        if cur == None:
            return pre
        else:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            return self.reverse(cur, pre)
