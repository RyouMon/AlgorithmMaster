/**
 * 24. 两两交换链表中的节点
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummyHead = new ListNode(0, head);
        ListNode cur = dummyHead;
        ListNode first;
        ListNode second;
        ListNode third;

        while (cur.next != null && cur.next.next != null) {
            first = cur.next;
            second = cur.next.next;
            third = cur.next.next.next;

            cur.next = second;
            second.next = first;
            first.next = third;

            cur = cur.next.next;
        }

        return dummyHead.next;
    }
}
