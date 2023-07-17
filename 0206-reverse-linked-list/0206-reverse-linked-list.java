/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode temp = head;
        ArrayList<Integer> arr = new ArrayList<Integer>();
        while(temp!=null){
            arr.add(temp.val);
            temp = temp.next;
            
        }
        ListNode reversedHead = null;
        ListNode current = null;
        for (int i = arr.size()-1 ; i >=0; i--) {
            if (reversedHead == null) {
                reversedHead = new ListNode(arr.get(i));
                current = reversedHead;
            } else {
                current.next = new ListNode(arr.get(i));
                current = current.next;
            }
        }
        return reversedHead; 
    }
}