# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution01:
    """
    直接使用原链表删除。
    """

    def removeElements(self, head: ListNode, val: int) -> ListNode:

        # 删除头节点
        while (head is not None) and (head.val == val):

            head = head.next

        # 删除其他节点
        current = head

        while (current is not None) and (current.next is not None):

            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head


class Solution02:
    """
    先添加虚拟头节点，再进行删除。
    """

    def removeElements(self, head: ListNode, val: int) -> ListNode:

        # 为链表设置虚拟头节点
        new_head = ListNode(None)
        new_head.next = head

        # 执行删除
        current = new_head

        while (current is not None) and (current.next is not None):

            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return new_head.next
