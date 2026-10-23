# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 0:
            return head
        length = 1
        temp2 = head
        while temp2.next:
            length+=1
            temp2=temp2.next
        k = k%length
        if k == 0:
            return head
        temp2.next = head
        steps = length-k
        curr = temp2
        while steps:
            curr=curr.next
            steps-=1
        newHead= curr.next
        curr.next=None
        return newHead
        


            
        
        