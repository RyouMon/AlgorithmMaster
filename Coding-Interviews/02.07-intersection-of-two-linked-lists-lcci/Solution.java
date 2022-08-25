/**
 * 面试题 02.07. 链表相交
 * 时间复杂度O(mn) 空间复杂度O(1)
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lengthA = 0;
        ListNode cur = headA;
        while (cur != null) {
            cur = cur.next;
            lengthA++;
        }

        int lengthB = 0;
        cur = headB;
        while (cur != null) {
            cur = cur.next;
            lengthB++;
        }
        
        ListNode longCur;
        ListNode shortCur;
        if (lengthA > lengthB) {
            longCur = headA;
            shortCur = headB;
        } else {
            longCur = headB;
            shortCur = headA;
        }

        for (int i = Math.abs(lengthA - lengthB); i > 0; i--) {
            longCur = longCur.next;
        }

        while (shortCur != null) {
            if (shortCur.equals(longCur)) {
                return shortCur;
            }
            shortCur = shortCur.next;
            longCur = longCur.next;
        }

        return null;
    }
}
