/**
 * 142. 环形链表 II
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            // 不能使用 fast.equals(slow)，因为 fast 可能先到达 null
            if (slow.equals(fast)) {
                ListNode index1 = head;
                ListNode index2 = fast;
                while (!index1.equals(index2)) {
                    index1 = index1.next;
                    index2 = index2.next;
                }
                return index1;
            }
        }
        return null;
    }
}
