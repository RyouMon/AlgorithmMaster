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
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # 获取头节点
        if (index == 0) and (self.size):
            return self.head.val
        # 获取其他节点
        elif 0 < index < self.size:
            cur = self.head
            for i in range(index):
                cur = cur.next
            return cur.val
        # index 不合法则返回 -1
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = self.Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.Node(val)
        cur = self.head
        if cur:
            while cur.next:
                cur = cur.next
            cur.next = node
        else:
            self.head = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # 头部插入
        if index == 0:
            self.addAtHead(val)
        # 尾部插入
        elif index == self.size:
            self.addAtTail(val)
        # 中间插入
        elif 0 < index < self.size:
            # 定位到插入位置的前一个节点
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            # 进行插入
            node = self.Node(val)
            tmp = cur.next
            cur.next = node
            node.next = tmp
            self.size += 1
        # 否则什么也不做
        else:
            return

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self.size:
            # 设置虚拟头节点
            tmp_head = self.Node(None)
            tmp_head.next = self.head
            # 遍历到被删除节点的前一个节点
            cur = tmp_head
            for i in range(index):
                cur = cur.next
            # 执行删除
            cur.next = cur.next.next
            self.head = tmp_head.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)