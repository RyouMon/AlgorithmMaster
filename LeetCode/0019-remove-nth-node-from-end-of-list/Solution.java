/**
 * 19. 删除链表的倒数第 N 个结点 双指针法
 * 时间复杂度 O(n) 空间复杂度 O(1)
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummyHead = new ListNode(-1, head);
        ListNode fast = dummyHead;
        ListNode slow = dummyHead;

        for (int i = 0; i < n + 1; i++) {
            fast = fast.next;
        }

        while (fast != null) { 
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;

        return dummyHead.next;
    }
}
