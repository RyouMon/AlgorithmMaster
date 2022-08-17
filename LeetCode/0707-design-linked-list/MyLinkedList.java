/**
 * 0707. 设计链表
 */
class MyLinkedList {
    
    LinkedNode dummyHead;
    int size;

    class LinkedNode {
        int val;
        LinkedNode next;

        public LinkedNode(int val) {
            this.val = val;
        }

        public LinkedNode(int val, LinkedNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public MyLinkedList() {
        size = 0;
        dummyHead = new LinkedNode(0);
    }
    
    public int get(int index) {
        if (index < 0 || index >= size) {
            return -1;
        }
        LinkedNode cur = dummyHead.next;
        while (index-- > 0) {
            cur = cur.next;
        }    
        return cur.val;
    }
    
    public void addAtHead(int val) {
        addAtIndex(0, val);;
    }
    
    public void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    public void addAtIndex(int index, int val) {
        if (index > size) {
            return;
        }
        LinkedNode cur = dummyHead;
        while (index-- > 0) {
            cur = cur.next;
        }
        LinkedNode node = new LinkedNode(val, cur.next);
        cur.next = node;
        size++;
    }
    
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return;
        }
        LinkedNode cur = dummyHead;
        while (index-- > 0) {
            cur = cur.next;
        }
        cur.next = cur.next.next;
        size--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */