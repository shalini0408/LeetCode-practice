# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        newHead = head
        length = 0
        while temp!=None:
            temp = temp.next
            length+=1
        middleNum = (length / 2) 
        i =0
        while i< middleNum:
            newHead = newHead.next
            i+=1
        return newHead

        