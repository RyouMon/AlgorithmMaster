/**
 * 206. 反转链表 双指针法
 */
class Solution1 {
    public ListNode reverseList(ListNode head) {
        ListNode pre = null;
        ListNode cur = head;
        ListNode next;  // 用于缓存下一个节点

        while (cur != null) {
            next = cur.next;
            cur.next = pre;  // 翻转
            pre = cur;
            cur = next;
        }

        return pre;
    }
}
