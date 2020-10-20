class MyLinkedList01:
    """
    单链表
    """

    class Node:

        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy_head = self.Node(0)  # 虚拟头节点
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if (index < 0) or (index >= self.size):
            return -1
        else:
            cur = self.dummy_head.next
            for _ in range(index):
                cur = cur.next
            return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = self.Node(val)
        node.next = self.dummy_head.next
        self.dummy_head.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur = self.dummy_head
        for _ in range(self.size):
            cur = cur.next
        cur.next = self.Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        else:
            cur = self.dummy_head
            for _ in range(index):
                cur = cur.next
            node = self.Node(val)
            node.next = cur.next
            cur.next = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if (index < 0) or (index >= self.size):
            return
        else:
            cur = self.dummy_head
            for _ in range(index):
                cur = cur.next
            cur.next = cur.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)