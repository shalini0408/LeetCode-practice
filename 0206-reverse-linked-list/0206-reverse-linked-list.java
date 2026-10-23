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
    if(head==null || head.next==null)return head;
      ListNode reverseHead = null;
      ListNode prev = head;
      ListNode temp = head;

      while(temp.next!=null){
        temp= prev.next;
        prev.next = reverseHead;
        reverseHead=prev;
        prev=temp;
      }  
      temp.next=reverseHead;
      reverseHead=temp;
      return reverseHead;
    }
}