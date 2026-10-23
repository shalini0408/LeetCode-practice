# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
        length =0
        temp=head
        while temp !=None:
            length+=1
            temp= temp.next
        if length == n:
            return head.next
        nThNode = length - n
        prev=head
        temp=head
        i=0
        while i<nThNode:
            prev= temp
            temp=temp.next
            i+=1
        prev.next = temp.next
        return head
        

        
        
        